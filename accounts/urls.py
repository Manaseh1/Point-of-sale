from django.urls import path
from accounts import views
from .views import *

appname = 'accounts'

urlpatterns = [
    path('',home,name='home'),
    path('Login/',views.signin,name='login'),
    path('profile/', views.profile, name='profile'),
]