from rest_framework import serializers
from .models import User

class Profileserializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()   

    class Meta: #the metadata class is used to specify the model and the fields that we want to include in the serializer
        model = User #connects the serializer to the User model
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers_count', 'following_count']
    def get_followers_count(self, obj):
        return obj.followers.count()    
    def get_following_count(self, obj):
        return obj.following.count()    
