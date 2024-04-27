from django.urls import path
from users.views import HomeView, SignInView, SignUpView, SignOutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signout/', SignOutView.as_view(), name='signout'),
]