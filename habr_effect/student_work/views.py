from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.

menu = ['Главная', 'Обратная связь', 'Кто мы?']

context = {
        'menu_main': 'Главная',
        'menu_feedback': 'Обратная связь',
        'menu_whoweare': 'Кто мы?',
        'title': 'Главная страница',
    }

url = {
    "index_url": "/",
    "whoweare": "/whoweare/",
    "feedback": "/feedback/",
}

# context = {
#     'menu_main': {'name': 'Главная', 'url': '/'},
#     'menu_whoweare': {'name': 'Кто мы?', 'url': '/whoweare/'},
#     'menu_feedback': {'name': 'Обратная связь', 'url': '/feedback/'},
# }


def index(request):

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


def dip_work(request, dip_id):

    html = f'<h1>Страница приложения student_work</h1><p>{dip_id}</p>'

    return HttpResponse(html)