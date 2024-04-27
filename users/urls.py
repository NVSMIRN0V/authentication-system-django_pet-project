from django.urls import path
from users.views import home, signin, signout, signup


urlpatterns = [
    path('', home, name='home'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='signout'),
]