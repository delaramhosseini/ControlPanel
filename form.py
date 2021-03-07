from django import forms
from django.forms import ModelForm
from .models import Video

class CreateVideo(ModelForm):
    class Meta:
        model = Video
        fields = '__all__'
