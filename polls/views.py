from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking forr question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're looking forr question %s" % question_id)