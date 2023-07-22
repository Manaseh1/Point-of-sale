from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from django.urls import reverse_lazy
from accounts.models import Profile
from django.views.generic.edit import UpdateView
from django.core.mail import send_mail

# Create your views here.


def employee_list(request):
    profile = Profile.objects.all()
    return render(request, 'emptable.html', {'profile': profile})


def add_employee(request):
    form = EmployeeCreationForm(request.POST)
    # detail = get_object_or_404(NewEmployee, id=employee_id)
    sent = False
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            subject = "These are your login credentials"
            message = f"""Your username is {cd['username']}. Your password is {cd['password1']}. Your role is {cd['role']}"""
            send_mail(subject,message,'manasehnjoroge7@gmail.com',[cd['email']])
            form.save()
            return redirect('employees:employee_list')
            sent = True
    context = {
        'form':form,
        'sent':sent,
    }       
            
    return render(request, 'employadd.html', context)




class edit_employee(UpdateView):
    template_name = 'employedit.html'
    form_class = EmployeeEditForm
    model = NewEmployee

    def get_success_url(self):
        return reverse_lazy('employee:employee_list')


def delete_employee(request, id):
    employee = NewEmployee.objects.get(id=id)
    employee.delete()
    return redirect('employees:employee_list')
