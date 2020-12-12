import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from exam.models import Question, Choice, Result


@login_required
def exam_result(request):
    if request.method == 'GET':
        return redirect('/')
    else:
        choices = Choice.objects.select_related()
        count = 0
        questions_count = 0

        for name, value in request.POST.items():
            if name.startswith('q_'):
                questions_count += 1
                for choice in choices:
                    if name.split('_')[1] == str(choice.fk_question_id.id) and value == str(choice.id) and choice.is_true:
                        count += 1

        user = User.objects.get(id=request.user.id)
        result = Result()
        result.fk_user_id = user
        result.result = count
        result.date = datetime.date.today()
        result.questions_count = questions_count
        result.save()

        context = {
            'questions_count': questions_count,
            'count': count,
        }

        return render(request, 'exam/result.html', context)


@login_required
def start_exam(request):
    if request.method == 'GET':
        questions = []
        choices = []

        for x in range(0, 3):
            questions += Question.objects.filter(id=x)
            choices += Choice.objects.filter(fk_question_id=x).select_related()

        context = {
            'questions': questions,
            'choices': choices,
        }

        return render(request, 'exam/start.html', context)
    else:
        return render(request, 'exam/start.html')
