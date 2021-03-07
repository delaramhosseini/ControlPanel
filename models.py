from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_data=models.DateTimeField('data published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_data <= now
    was_published_recently.admin_order_field = 'pub_data'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_data <= now


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
