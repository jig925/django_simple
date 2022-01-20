from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice
from django.template import loader
# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }

    return render(request, 'detail.html', context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def showQuestionChoices(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    values = choices.values()
    result = set()

    for _, choice in enumerate(values):
        result.add(choice["choice_text"])

    response = f"Choices for question {question.id}: {str(result)}"

    context = {
        'choice_text':result
    }

    print("RESULT",result)

    return render(request,"choices.html", context)
