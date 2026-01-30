from django.db import models
from django.contrib.auth.models import User


class ShortedUrl(models.Model):
    long_url = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    no_of_clicks = models.IntegerField(default = 0)

class AdditionalUserInfo(models.Model):
    user = models.OneToOneField(User, related_name = 'additional', on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to = 'photos/', default = 'default.png')
