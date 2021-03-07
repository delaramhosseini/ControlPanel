from django.contrib import admin
from .models import *


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_data']}),
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Video)
admin.site.register(Exercise)
admin.site.register(Answer)
