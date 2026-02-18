from django.urls import path,include
from .views import ProfileView, RegisterView, CustomAuthToken
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .views import FollowUserView, UnfollowUserView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('', include(router.urls)),  # Include the router URLs for user profiles

    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]
