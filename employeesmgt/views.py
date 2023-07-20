from django.shortcuts import render,redirect
from .forms import *
from django.urls import reverse_lazy
from accounts.models import Profile
from django.views.generic.edit import UpdateView


# Create your views here.
def employee_list(request):
    profile = Profile.objects.all()
    return render(request,'emptable.html',{'profile':profile})

def add_employee(request):
    form = EmployeeCreationForm(request.POST)
    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees:employee_list')
    return render(request,'employadd.html',{'form':form})

class edit_employee(UpdateView):
    template_name = 'employedit.html'
    form_class = EmployeeEditForm
    model = NewEmployee
    def get_success_url(self):
        return reverse_lazy('employee:employee_list')


def delete_employee(request,id):
    employee = NewEmployee.objects.get(id= id)
    employee.delete()
    return redirect('employees:employee_list')