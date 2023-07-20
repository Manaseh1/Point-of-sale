from django.shortcuts import render,redirect
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
@login_required(login_url='login')
def CustomersMgtDashboard(request):
    
    context = {

    }
    return render(request, 'customers.html', context)
@login_required(login_url='login')
def underdev(request):
    
    context = {

    }
    return render(request, 'underdev.html', context)


