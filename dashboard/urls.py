from django.urls import path
from dashboard import views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


appname = 'dashboard'

urlpatterns = [
    path('index/', views.dashboard, name='index'),
    path('logout/', views.logout_view, name='logout'),
]