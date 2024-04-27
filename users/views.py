from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'users/index.html', context={'title': 'Главная'})


def signin(request: HttpRequest) -> HttpResponse:
    return render(request, 'users/signin.html', context={'title': 'Войти'})


def signup(request: HttpRequest) -> HttpResponse:
    return render(request, 'users/signup.html', context={'title': 'Зарегистрироваться'})


def signout(request: HttpRequest) -> HttpResponse:
    return render(request, 'users/signout.html', context={'title': 'Выйти'})
