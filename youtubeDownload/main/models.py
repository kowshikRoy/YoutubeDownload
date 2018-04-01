from django.db import models

class Playlist(models.Model):
    id = models.CharField(max_length = 100, unique = True, primary_key = True)
    ncounts = models.IntegerField(default = 0)
    name = models.CharField(max_length = 300)

class Video(models.Model):
    id = models.CharField(max_length = 100, unique = True, primary_key = True)
    duration = models.IntegerField(default = 0)
    title = models.CharField(max_length = 300)
    fps = models.IntegerField(default = 1)
    thumbnail = models.CharField(max_length = 300)
    playlist_index = models.IntegerField(null = True)
    playlist = models.ForeignKey(Playlist, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.title



class Url(models.Model):
    url = models.CharField(max_length = 1000)
    size = models.FloatField(default = 0)
    ext = models.CharField(max_length = 10)
    vcodec = models.BooleanField(default = False)
    acodec = models.BooleanField(default = False)
    format_id = models.IntegerField(default = 43)
    height = models.IntegerField(default = 0)
    width = models.IntegerField(default = 0)
    video = models.ForeignKey(Video, on_delete = models.CASCADE)
    def __str__(self):
        return self.video.title+'.'+ self.ext +'('+ str(self.size) + ')'
    class Meta:
        ordering= ['-height']


    







