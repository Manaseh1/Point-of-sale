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
from stockmgt.models import Stock
@login_required(login_url='login')
def dashboard(request):
    low_quantity_stocks = Stock.objects.filter(remaining_quantity__lt=10)
    count = low_quantity_stocks.count()
    has_low_quantity = count > 0
    current_site = get_current_site(request)
    context = {
        'has_low_quantity': has_low_quantity,
        'low_quantity_count': count,
        'current_site': current_site,
    }

    return render(request, 'dashboard.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:login')
