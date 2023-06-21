from django.urls import path
from accounts import views

appname = 'accounts'

urlpatterns = [
    path('', views.landingpage, name='Home'),
]