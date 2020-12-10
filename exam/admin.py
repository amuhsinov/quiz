from django.contrib import admin

# Register your models here.
from django.forms import forms

from exam.models import Question, Choice


class ShowQuestion(admin.ModelAdmin):
    list_display = ['id', 'question']


class ShowChoice(admin.ModelAdmin):
    list_display = ['fk_question_id_id', 'choice', 'is_true']


admin.site.register(Question, ShowQuestion)
admin.site.register(Choice, ShowChoice)
