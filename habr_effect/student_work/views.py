from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Dip_work
# Create your views here.

menu = ['Главная', 'Обратная связь', 'Кто мы?']

context = {
        'menu_main': 'Главная',
        'menu_feedback': 'Обратная связь',
        'menu_whoweare': 'Кто мы?',
        'title': 'Главная страница',
        'articles': '',
    }


def index(request):

    articles = Dip_work.objects.all()
    context = {
        'articles': articles
    }

    if request.method == 'POST':
        return redirect('/')

    return render(request, 'student_work/main.html', context)


def whoweare(request):

    context['title'] = 'Кто мы?'

    if request.method == 'POST':
        return redirect('/whoweare/')

    return render(request, 'student_work/whoweare.html', context)


def feedback(request):

    context['title'] = 'Обратная связь'

    if request.method == 'POST':
        return redirect('/feedback/')

    return render(request, 'student_work/feedback.html', context)


def dip_work_page(request, dip_id):

    article = get_object_or_404(Dip_work, id=dip_id)
    context = {
        'article': article
    }

    return render(request, 'student_work/dipworkpage.html', context)