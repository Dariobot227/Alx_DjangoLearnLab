
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import ProfileSerializer
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provides:
    - list users
    - retrieve user profile
    - custom follow/unfollow actions
    """

    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def follow(self, request, pk=None):
        """
        Current user follows the target user.
        """
        target_user = get_object_or_404(User, pk=pk)

        if target_user == request.user:
            return Response(
                {"error": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        request.user.following.add(target_user)

        return Response(
            {"message": f"You are now following {target_user.username}."},
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=['post'])
    def unfollow(self, request, pk=None):
        """
        Current user unfollows the target user.
        """
        target_user = get_object_or_404(User, pk=pk)

        request.user.following.remove(target_user)

        return Response(
            {"message": f"You have unfollowed {target_user.username}."},
            status=status.HTTP_200_OK
        )
