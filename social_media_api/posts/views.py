from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# -----------------------------
# Permissions
# -----------------------------
class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Only authors can edit or delete their own posts/comments.
    Others can only read (GET requests).
    """
    def has_object_permission(self, request, view, obj):
        # Safe methods: GET, HEAD, OPTIONS are allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write methods allowed only for author
        return obj.author == request.user


# -----------------------------
# Post ViewSet
# -----------------------------
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')  # Show newest first
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]  # Read-only for unauthenticated

    filter_backends = [filters.SearchFilter]  # Enable search
    search_fields = ['title', 'content']      # Allow searching by title or content

    def perform_create(self, serializer):
        """
        Automatically set the logged-in user as the author of a post.
        This ensures the client cannot set the author manually.
        """
        serializer.save(author=self.request.user)


# -----------------------------
# Comment ViewSet
# -----------------------------
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        """
        Automatically set the logged-in user as the author when creating a comment.
        """
        serializer.save(author=self.request.user)

