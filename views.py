from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .models import *
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth,redirects
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from app1.form import *
from django.contrib.auth import login,authenticate
from django.template import RequestContext


def home(request):
    text={}
    return render(request, 'app1/home.html', text)


def teacher_home(request):
    text ={}
    return render(request, 'app1/teacher_home.html', text)

def student_home(request):
    text={}
    return render(request, 'app1/student_home.html', text)

def teacher_video(request):
    videos = Video.objects.all()
    text={'videos': videos}
    return render(request, 'app1/videos.html', text)

def student_video(request):
    videos =Video.objects.all()
    text={'videos': videos}
    return render(request, 'app1/student_video.html', text)

def student_exercise(request):
    exercises = Exercise.objects.all()
    text = {'exercises': exercises}
    return render(request, 'app1/student_exercise.html', text)

def teacher_exercise(request):
    exercises = Exercise.objects.all()
    text = {'exercises': exercises}
    return render(request, 'app1/teacher_exercise.html', text)

def teacher_upload_exercise(request):
    form=CreateExercise()
    if request.method=='POST':
        form =CreateExercise(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('your file has been uploaded')
    else:
        text={'form': form }
        return render(request, 'app1/teacher_upload_exercise.html', text)


def teacher_upload(request):
    form= CreateVideo()
    if request.method=='POST':
        form =CreateVideo(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('your file has been uploaded')
    else:
        text={'form': form }
        return render(request, 'app1/teacher_upload.html', text)

def student_answer(request):
    form= CreateAnswer()
    if request.method=='POST':
        form =CreateAnswer(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('your file has been uploaded')
    else:
        text={'form': form }
        return render(request, 'app1/student_answer.html', text)

def video_detail(request,video_id):
    vid = Video.objects.get(id=video_id)
    text={'video':vid}
    return render(request, 'app1/video_detail.html', text)

def exercise_detail(request, exercise_id):
    exer = Exercise.objects.get(id=exercise_id)
    text={'exercise':exer}
    return render(request, 'app1/exercise_detail.html', text)


def exercise_detail_teacher(request, exercise_id):
    exer = Exercise.objects.get(id=exercise_id)
    text={'exercise':exer}
    return render(request, 'app1/exercise_detail_teacher.html', text)


