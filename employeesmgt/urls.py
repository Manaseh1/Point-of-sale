from django.urls import path
from .views import *

app_name = 'employee'
urlpatterns = [
    path('employee_list/',employee_list,name='employee_list'),
    path('employee_add/',add_employee,name='employee_add'),
    path('employee_delete/<int:id>/',delete_employee,name='employee_delete'),
    path('employee_edit/<pk>/',edit_employee.as_view(),name='employee_edit'),
    
    
    # path('employee_edit/<pk>/',edit_employee,name='edit_employee'),
    
]