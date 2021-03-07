import django
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app1'
urlpatterns = [
    path('', views.home, name='home'),
    path('teacher_home/',views.teacher_home, name='teacher_home'),
    path('student_home', views.student_home, name='student_home'),
    path('student_video/', views.student_video, name='student_video'),
    path('student_video/<int:video_id>', views.video_detail, name = 'video_detail'),
    path('teacher_video/', views.teacher_video, name='teacher_video'),
    path('teacher_video/upload', views.teacher_upload, name = 'teacher_upload'),
    path('teacher_video/<int:video_id>', views.video_detail, name = 'video_detail'),
    path('teacher_exercise/', views.teacher_exercise, name='teacher_exercise'),
    path('teacher_exercise/upload', views.teacher_upload_exercise, name='teacher_upload_exercise'),
    path('teacher_exercise/<int:exercise_id>', views.exercise_detail_teacher, name = 'exercise_detail_teacher'),
    path('student_exercise/', views.student_exercise, name='student_exercise'),
    path('student_exercise/upload', views.student_answer, name='student_answer'),
    path('student_exercise/<int:exercise_id>', views.exercise_detail, name = 'exercise_detail'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
