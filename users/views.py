from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

from django.shortcuts import render
from django.urls import reverse_lazy

from users.forms import UserSignInForm, UserSignUpForm


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/index.html', context={'title': 'Главная'})


class SignInView(LoginView):
    form_class = UserSignInForm
    template_name = 'users/signin.html'
    next_page = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Войти'
        return context


class SignUpView(CreateView):
    form_class = UserSignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('signin')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context


class SignOutView(LogoutView):
    template_name = "users/signout.html"
    next_page = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Выйти'
        return context