from django.contrib import admin
from .models import Emotion, Music
import embed_video
from embed_video.admin import AdminVideoMixin
# Register your models here.


class PostAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('title', 'video', 'emotion_code')

admin.site.register(Music, PostAdmin)