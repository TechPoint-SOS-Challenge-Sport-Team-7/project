from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    message = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    player = models.CharField(max_length=30)
    playerName = models.CharField(max_length=50)
    response = models.CharField(max_length=300)
    answered = models.BooleanField()
    def __str__(self):
        return self.message

class AnsweredQuestions(models.Model):
    message = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    player = models.CharField(max_length=30)
    playerName = models.CharField(max_length=50)
    response = models.CharField(max_length=300)
    def __str__(self):
        return self.message

class Player(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=3)
    position = models.CharField(max_length=50)
    college = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    following = models.BooleanField()

    def __str__(self):
        return str(self.name)
    def isFollowing(self):
        pass


class UserFollowing(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="flw", null=True)
    username = models.CharField(max_length=20)
    playerName = models.CharField(max_length=50)
    following = models.BooleanField()
    def __str__(self):
        return str(self.username)



class MovieInfo(models.Model):
    title = models.CharField(max_length=200)


