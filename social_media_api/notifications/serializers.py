from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    target_title = serializers.CharField(source='target.title', read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'actor_username', 'verb', 'target_title', 'timestamp', 'is_read']
