import django
from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('teacher_home/',views.teacher_home, name='teacher_home'),
    path('student_home', views.student_home, name='student_home'),
    path('teacher_video/', views.teacher_video, name='teacher_video'),
    path('teacher_video/upload', views.teacher_upload, name = 'teacher_upload'),
]
