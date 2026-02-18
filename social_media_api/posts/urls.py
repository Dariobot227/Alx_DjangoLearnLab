from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

# -----------------------------
# DRF Routers for standard CRUD
# -----------------------------
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

# -----------------------------
# Explicit URL patterns for feed and like/unlike
# -----------------------------
urlpatterns = [
    path('', include(router.urls)),              # Include router URLs (CRUD)
    path('feed/', FeedView.as_view(), name='feed'),  # User feed endpoint

    # Explicit like/unlike URLs 
    path('posts/<int:pk>/like/', PostViewSet.as_view({'post': 'like'}), name='post-like'),
    path('posts/<int:pk>/unlike/', PostViewSet.as_view({'post': 'unlike'}), name='post-unlike'),
]
