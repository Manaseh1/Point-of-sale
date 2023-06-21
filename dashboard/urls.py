from django.urls import path
from dashboard import views

appname = 'dashboard'

urlpatterns = [
    path('', views.landingpage, name='Dashboard'),
]