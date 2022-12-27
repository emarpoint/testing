from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from testapp.models import Profile, Category, Question
from django.contrib.auth import get_user_model

User = get_user_model()


# def test_start(request,):
#         questions = Question.objects.all()
#         context = {
#             'questions': questions,
#         }
#         template = 'answer/test_start.html'
#         return render(request, template, context)


def test_startt(request,):

    questions = list(Question.objects.values_list('question', flat=True))
    # questions = q[0]
    # print(questions)
    questi = Question.objects.all()
    print(questi)
   
   
   
   
   
   
   
    context = {

        'questions': questions,
    }
    # print(context)
    template = 'answer/test_start.html'
    return render(request, template, context)

def test_start(request):
    if request.method == 'POST':
        print(request.POST)
        questions=Question.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.answer)
            if q.answer ==  request.POST.get(q.question):
                score+=10
                correct+=1
                print(correct)
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        template = 'answer/result.html'
        return render(request, template, context)
    else:
        questions=Question.objects.all()
        context = {
            'questions':questions
        }
        template = 'answer/test_start.html'
        return render(request, template, context)