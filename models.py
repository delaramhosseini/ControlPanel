from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class Video(models.Model):
    caption = models.CharField(max_length=100)
    vids  = models.FileField(upload_to='video')

    def __str__(self):
        return self.caption

class Exercise(models.Model):
    caption=models.CharField(max_length=200)
    exercise = models.FileField(upload_to='exercise')

    def __str__(self):
        return self.caption


class Answer(models.Model):
    caption =models.CharField(max_length=200)
    answer = models.FileField(upload_to='answer')

    def __str__(self):
        return self.caption

