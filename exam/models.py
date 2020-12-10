from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question = models.TextField()


class Choice(models.Model):
    fk_question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.TextField()
    is_true = models.BooleanField()


class Result(models.Model):
    fk_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.IntegerField()
    date = models.DateField()
