from django.urls import path
from customersmgt import views
from .views import *



app_name = 'customersmgt'

urlpatterns = [
    path('CustomersDashboard', views.CustomersMgtDashboard, name='customers_dashboard'),
    path('underdev', views.underdev, name='underdev'),

]