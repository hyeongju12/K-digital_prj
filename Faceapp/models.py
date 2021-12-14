from django.db import models
from django.db.models.fields.files import FileField
import embed_video
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User


# Create your models here.
class Emotion(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=10)
    emotion_dt = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content_str = models.CharField(max_length=50, null=True)
    comment = models.TextField(null=True)

class Music(models.Model):
    title = models.CharField(max_length=30)
    video = EmbedVideoField()
    emotion_code = models.CharField(max_length=10)
