# posts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

# Create a DRF router
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')       # CRUD for posts
router.register(r'comments', CommentViewSet, basename='comment')  # CRUD for comments

urlpatterns = router.urls
# Include router URLs in urlpatterns
urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),  # User feed endpoint
]
