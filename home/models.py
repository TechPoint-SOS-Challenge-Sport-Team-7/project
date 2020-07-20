from django.db import models


class Information(models.Model):
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.message


class MovieInfo(models.Model):
    title = models.CharField(max_length=200)


