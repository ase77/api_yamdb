from rest_framework import serializers, exceptions
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import AccessToken

from review.models import (
    Review, Comment, Category, Genre, Title, User, UserRole
)


class BaseUserSerializer:
    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('wrong username.')
        return value

    def validate_role(self, value):
        if self.instance and self.instance.role == UserRole.USER:
            return UserRole.USER
        return value


class UserSignUpSerializer(BaseUserSerializer, serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email']


class UserSerializer(BaseUserSerializer, serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        ]


class TokenSerializer(TokenObtainSerializer):
    token_class = AccessToken

    def __init__(self, *args, **kwargs):
        super(serializers.Serializer, self).__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields["confirmation_code"] = serializers.CharField()

    def validate(self, attrs):
        data = {}
        username = attrs['username']
        confirmation_code = attrs['confirmation_code']

        try:
            self.user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.NotFound(
                'No user with such username.'
            )

        if self.user.confirmation_code != confirmation_code:
            raise exceptions.ValidationError(
                'No user with such credentials.'
            )

        token = self.get_token(self.user)
        data['token'] = str(token)
        return data


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ['id', 'text', 'author', 'score', 'pub_date']
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ['id', 'text', 'author', 'pub_date']
        model = Comment


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name', 'slug']
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name', 'slug']
        model = Genre


class StrToDictData(serializers.SlugRelatedField):

    def to_representation(self, obj):
        data_dict = {"name": obj.name, "slug": obj.slug}
        return data_dict


class TitleSerializer(serializers.ModelSerializer):
    genre = StrToDictData(
        many=True,
        slug_field='slug',
        queryset=Genre.objects.all()
    )
    category = StrToDictData(
        slug_field='slug',
        queryset=Category.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Title
