from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    """this extends django default user model, it adds the additional
        fields below ie:bio, profile pic and the followers

    """
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    #a user can have followers and can also follow other users.
    #symmetrical=False means that if user A follows user B, it does not imply that user B follows user A.
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    def __str__(self):
        return self.username
