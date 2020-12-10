from django.shortcuts import render

from exam.models import Question, Choice


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
