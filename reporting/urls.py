from django.urls import path
from reporting import views
from .views import *

app_name = 'reporting'
urlpatterns = [
    path('ReportDashboard', views.ReportsDashboard, name='report_dashboard'),
    path('fetch-data-from-database/', fetch_data_from_database, name='fetch-data-from-database'),
]