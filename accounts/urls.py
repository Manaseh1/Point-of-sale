from django.urls import path
from accounts import views
from .views import *

appname = 'accounts'

urlpatterns = [
    path('',home,name='home'),
    path('Login/',signin,name='login'),
]