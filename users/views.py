from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f'Home page.')


def signin(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f'Sign in page.')


def signup(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f'Sign up page.')


def signout(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f'Sign out page.')
