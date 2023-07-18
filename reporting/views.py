from collections import Counter
from os import truncate
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
from django.http import JsonResponse
from sales.models import MoneyControl, Sales
from django.db.models import Sum
from django.db.models import Count
from django.db.models.functions import TruncDate

def fetch_data_from_database(request):
    # Retrieve the Mpesa and Cash values from the database
    Mpesa = MoneyControl.objects.filter(payment_method = "Mpesa")
    Cash = MoneyControl.objects.filter(payment_method = "Cash")
    totalMpesa = Mpesa.aggregate(total=Sum('Amount'))['total'] or 0
    totalCash = Cash.aggregate(total=Sum('Amount'))['total'] or 0
    # Perform the query to filter and count sales by day
    sales_by_day = Sales.objects.annotate(date=TruncDate('date_added')).values('date').annotate(count=Count('id')).order_by('date')

    # Extract the dates and counts from the queryset
    dates = [sale['date'].strftime('%Y-%m-%d') for sale in sales_by_day]
    counts = [sale['count'] for sale in sales_by_day]

    # Return the dates and counts as JSON response
    data = {
        'dates': dates,
        'counts': counts,
        'mpesa': totalMpesa or 0,
        'cash': totalCash or 0
    }
    return JsonResponse(data)

@login_required(login_url='login')
def ReportsDashboard(request):
    Mpesa = MoneyControl.objects.filter(payment_method = "Mpesa")
    Cash = MoneyControl.objects.filter(payment_method = "Cash")
    totalMpesa = Mpesa.aggregate(total=Sum('Amount'))['total'] or 0
    totalCash = Cash.aggregate(total=Sum('Amount'))['total'] or 0

    # Return the values as JSON response
    context = {
        'mpesa': totalMpesa or 0,
        'cash': totalCash or 0
    }
    return render(request, 'reports.html', context)