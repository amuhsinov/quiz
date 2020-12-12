from django import forms

from exam.models import Question, Choice


class QuizForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'

