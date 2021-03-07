from django import forms
from django.forms import ModelForm
from .models import *

class CreateVideo(ModelForm):
    class Meta:
        model = Video
        fields = '__all__'


class CreateExercise(ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'

class CreateAnswer(ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'

