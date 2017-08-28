from django.db import models
from django.core.urlresolvers import reverse


class Album(models.Model):
    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField(max_length=500)
    is_favorite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    song_title = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)
    audio = models.FileField(max_length=500)

    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk': self.album_id})

    def __str__(self):
        return self.song_title


class Video(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, default="Mugen")
    video_title = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)
    video = models.FileField(max_length=500)

    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk': self.album_id})

    def __str__(self):
        return self.video_title

