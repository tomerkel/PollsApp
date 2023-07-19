from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import Question
from django.template import loader, RequestContext
from django.urls import reverse


def index(request):
    latest_questions = Question.objects.order_by('-publish_date')[:5]
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def result(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': q})


def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', {'question': q, 'error_message': "Please select a choice"})
    else:
        selected_choice.votes_number += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:result', args={question_id, }))

