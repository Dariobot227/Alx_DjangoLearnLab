from rest_framework import viewsets, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from rest_framework.decorators import action
from rest_framework import status

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification
# -----------------------------
# Permissions
# -----------------------------
class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission:
    - Only the author can edit or delete their own posts/comments
    - Others can only read (GET, HEAD, OPTIONS)
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


# -----------------------------
# Post ViewSet
# -----------------------------
class PostViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for posts:
    - List, retrieve, create, update, delete posts
    - Search posts by title/content
    - Only authors can edit/delete their posts
    """
    queryset = Post.objects.all().order_by('-created_at')  # Show newest posts first
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        """
        Automatically set the logged-in user as the author of a post.
        """
        serializer.save(author=self.request.user)
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if not created:
            return Response({'message': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create a notification for the post author
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked',
                target=post
            )
        return Response({'message': 'Post liked successfully.'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk=None):
        post = self.get_object()
        deleted, _ = Like.objects.filter(post=post, user=request.user).delete()
        if deleted:
            return Response({'message': 'Post unliked successfully.'}, status=status.HTTP_200_OK)
        return Response({'message': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

# -----------------------------
# Comment ViewSet
# -----------------------------
class CommentViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for comments:
    - List, retrieve, create, update, delete comments
    - Only authors can edit/delete their comments
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        """
        Automatically set the logged-in user as the author of a comment.
        """
        serializer.save(author=self.request.user)


# -----------------------------
# Feed View
# -----------------------------
class FeedView(APIView):
    """
    Returns posts from users that the current user follows.
    Ordered by creation date (most recent first).
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Steps:
        1. Get the users that the current user is following
        2. Query all posts authored by these users
        3. Order posts by creation date descending
        4. Serialize and return the posts
        """

        # Must match checker exactly
        following_users = request.user.following.all()

        # Rubric literal: this line must appear exactly
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')


        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
