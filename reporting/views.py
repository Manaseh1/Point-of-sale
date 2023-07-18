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
from sales.models import MoneyControl, Sales, salesItems
from stockmgt.models import Stock
from django.db.models import Count
from django.db.models.functions import TruncDate

from django.db.models import Sum

def fetch_data_from_database(request):
    # Retrieve the Mpesa and Cash values from the database
    Mpesa = MoneyControl.objects.filter(payment_method="Mpesa")
    Cash = MoneyControl.objects.filter(payment_method="Cash")
    totalMpesa = Mpesa.aggregate(total=Sum('Amount'))['total'] or 0
    totalCash = Cash.aggregate(total=Sum('Amount'))['total'] or 0

    # Perform the query to filter and count sales by day
    sales_by_day = Sales.objects.annotate(date=TruncDate('date_added')).values('date').annotate(count=Count('id')).order_by('date')

    # Extract the dates and counts from the queryset
    dates = [sale['date'].strftime('%Y-%m-%d') for sale in sales_by_day]
    counts = [sale['count'] for sale in sales_by_day]

    # Retrieve the top products data
    top_products = salesItems.objects.values('product').annotate(
        sales_count=Count('sale', distinct=True),
        total_quantity=Sum('qty')
    ).order_by('-sales_count', '-total_quantity')[:7]

    # Prepare the top products data for the response
    products_data = []
    for product in top_products:
        product_data = {
            'product': product['product'],
            'sales_count': product['sales_count'],
            'total_quantity': product['total_quantity'],
        }
        products_data.append(product_data)

    # Retrieve the critical stock data
    critical_stock = Stock.objects.filter(remaining_quantity__lt=10)
    critical_stock_data = [
        {
            'product': stock.product.name,
            'remaining_quantity': stock.remaining_quantity
        }
        for stock in critical_stock
    ]

    # Return the dates, counts, and other data as JSON response
    data = {
        'dates': dates,
        'counts': counts,
        'mpesa': totalMpesa or 0,
        'cash': totalCash or 0,
        'top_products': products_data,
        'critical_stock': critical_stock_data,
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
