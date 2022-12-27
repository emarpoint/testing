from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Profile, Category, Question
from django.contrib.auth import get_user_model

User = get_user_model()

def index(request):
    profile = Profile.objects.all()
    category = Category.objects.all()


#     page_obj = paginator(request, post_list)
    context = {
        'category': category,
        'profile': profile,
        'index': True,
    }
    return render(request, 'index.html', context)

     
# def cart_detail_test(request, test_id):
#     profile = get_object_or_404(Profile, id=test_id)

#     answer = Answer.objects.all()
#     question = Question.objects.all()
#     print(question)

#     context = {
#         'profile': profile,
#         'answer': answer,
#         'question': question,

#     }
#     template = 'testapp/cart_detail_test.html'
#     return render(request, template, context)

def test_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    profile = Profile.objects.filter()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        profile = profile.filter(category=category)
        
        
    context = {
        'category': category,
        'categories': categories,
        'profile': profile}

    
    template = 'testapp/test_list.html'
    return render(request, template, context)


def test_detail(request, id, slug):
    profile = get_object_or_404(Profile, id=id, slug=slug)       
    context = {
        'profile': profile,
    }
    template = 'testapp/test_detail.html'
    return render(request, template, context)


