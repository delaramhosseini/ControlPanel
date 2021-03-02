from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello,'
                        ' welcome to control panel,'
                        ' this is the home page')
# Create your views here.
