from django.contrib import admin

from .models import Playlist,Video,Url

admin.site.register(Video)
admin.site.register(Url)
admin.site.register(Playlist)
# Register your models here.
