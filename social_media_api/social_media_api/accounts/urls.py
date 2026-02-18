from django.urls import path
from .views import ProfileView, RegisterView, CustomAuthToken

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile', ProfileView.as_view(), name='profile'),
]
