from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import Http404
from django.http import HttpResponse

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def index2(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
        'route_name': 'index-2',
    }
    return HttpResponse(template.render(context, request))

def index3(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
            'latest_question_list': latest_question_list,
            'route_name': 'index-3',
            }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def detail2(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', 
            {
                'question': question,
                'detail_no' : 2 
            }
        )


def detail3(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {
                'question': question,
                'detail_no' : 3 
            })

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
