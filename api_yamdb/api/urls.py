from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import (
    ReviewViewSet,
    CommentViewSet,
    CategoryViewSet,
    GenreViewSet,
    TitileViewSet,
    UserModelViewSet,
    UserRegistrationView,
    TokenObtainView,
    MeView
)

router_v1 = DefaultRouter()

router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments')
router_v1.register('categories', CategoryViewSet)
router_v1.register('genres', GenreViewSet)
router_v1.register('titles', TitileViewSet)
router_v1.register('users', UserModelViewSet)


urlpatterns = [
    path('v1/auth/signup/', UserRegistrationView.as_view()),
    path('v1/auth/token/', TokenObtainView.as_view()),
    path('v1/users/me/', MeView.as_view()),
    path('v1/', include(router_v1.urls)),
]
