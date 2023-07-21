from django.shortcuts import render,redirect
from .forms import *
from django.urls import reverse_lazy
from accounts.models import Profile
from django.views.generic.edit import UpdateView
from django.core.mail import EmailMessage,send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import random
import string

# Create your views here.
def employee_list(request):
    profile = Profile.objects.all()
    return render(request,'emptable.html',{'profile':profile})

def add_employee(request):
    form = EmployeeCreationForm(request.POST)
    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Generate a random temporary password
            temp_password = generate_random_password()

            # Set the temporary password for the user
            user.set_password(temp_password)
            user.save()

            # Sending the welcome email to the new employee
            current_site = get_current_site(request)
            subject = 'Welcome to our company!'
            message = f'''
                Welcome, {user.username}!

                Thank you for joining our company.
                Your username is: {user.username}
                Your temporary password is: {temp_password}

                Please log in using the temporary password and change it after logging in.

                Click here to log in: {current_site.domain}/accounts/login/
            '''
            from_email = 'manasehnjoroge7@gmail.com'  # Replace with your company's email
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list)

            return redirect('employees:employee_list')
    return render(request, 'employadd.html', {'form': form})

def generate_random_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

class edit_employee(UpdateView):
    template_name = 'employedit.html'
    form_class = EmployeeEditForm
    model = NewEmployee
    
    def get_success_url(self):
        return reverse_lazy('employee:employee_list')


def delete_employee(request,id):
    employee = NewEmployee.objects.get(id= id)
    employee.delete()
    user = employee
    # Sending the welcome email to the new employee
    current_site = get_current_site(request)
    subject = 'Good BYE!'
    message = f'''
        Hello, {user.username}!
        your contract with our company have been terminated, sorry!.
        
    '''
    from_email = 'manasehnjoroge7@gmail.com'  # Replace with your company's email
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)
    return redirect('employees:employee_list')