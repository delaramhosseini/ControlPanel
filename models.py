from django.db import models
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_data=models.DateTimeField('data published')

class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_Text=models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

