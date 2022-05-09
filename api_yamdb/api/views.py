import uuid

from rest_framework import views, viewsets, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from rest_framework_simplejwt.views import TokenViewBase

from review.models import Title, Review, Comment, Category, Genre, User
from .permissions import AdminOrReadOnly, AuthOrReadOnly, AdminOnly
from .serializers import (
    CategorySerializer,
    CommentSerializer,
    GenreSerializer,
    ReviewSerializer,
    TitleSerializer,
    UserSerializer,
    UserSignUpSerializer,
    TokenSerializer
)


class UserRegistrationView(views.APIView):
    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            confirmation_code = str(uuid.uuid4())
            serializer.save(confirmation_code=confirmation_code)
            self.send_confirmation_email(
                serializer.data['email'], confirmation_code
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_confirmation_email(self, email, confirmation_code):
        send_mail(
            subject='Confirmation code',
            message=confirmation_code,
            from_email=settings.AUTH_EMAIL,
            recipient_list=[email]
        )


class TokenObtainView(TokenViewBase):
    serializer_class = TokenSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (permissions.IsAuthenticated, AdminOnly)


class MeView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        serializer = UserSerializer(
            request.user, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (
        AuthOrReadOnly, permissions.IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        return title.reviews.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        AuthOrReadOnly, permissions.IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, pk=review_id, title=title)
        return Comment.objects.filter(review=review)

    def perform_create(self, serializer):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, pk=review_id)
        serializer.save(author=self.request.user, review=review)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        AdminOrReadOnly
    )


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        AdminOrReadOnly
    )


class TitileViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (AdminOrReadOnly,)
