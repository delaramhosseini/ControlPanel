from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth,redirects
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

class IndexView(generic.ListView):
    template_name = 'app1/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_data__lte=timezone.now()).order_by('-pub_data')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'app1/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_data__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'app1/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'app1/detail.html', {'question': question,'error_message': "You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('app1:login'))



def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirects('allproducts')
        else:
            return render(request, 'app1/login.html', {'error':'Invalid Username Or Password'})
    else:
        return render(request, 'app1/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirects('index')

def upload(request):
    if request.method=='post':
        uploaded_file= request.FILES['document']
        fs= FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'app1/upload.html')
