from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token
from django.contib.auth import get_user_model

class ProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()   

    class Meta: #the metadata class is used to specify the model and the fields that we want to include in the serializer
        model = User #connects the serializer to the User model
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers_count', 'following_count']
    def get_followers_count(self, obj):
        return obj.followers.count()    
    def get_following_count(self, obj):
        return obj.following.count() 

#serializer that handles user registartion
  
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # <- THIS IS REQUIRED

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Create a new user securely
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )

        # Create a token for this user immediately
        Token.objects.create(user=user)

        return user