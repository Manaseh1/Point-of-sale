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
def inventory_dashboard(request):
    current_site = get_current_site(request)
    context = {
        'current_site': current_site,
    }

    return render(request, 'inventory_dashboard.html', context)