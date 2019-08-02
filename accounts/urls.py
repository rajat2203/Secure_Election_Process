from django.urls import path
from . import views

urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('govote', views.govote, name='govote'),
    path('logout', views.logout, name='logout')
]
