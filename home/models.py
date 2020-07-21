from django.db import models

class Information(models.Model):
    message = models.CharField(max_length=200)
    def __str__(self):
        return self.message

from embed_video.fields import EmbedVideoField

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()