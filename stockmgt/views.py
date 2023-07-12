from inventory.models import Product
from .models import *
from django.shortcuts import render, get_object_or_404,redirect

def restock(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)

    return render(request, 'stock_management/restock.html', {'stock': stock})

def stock_alerts(request):
    low_quantity_stocks = Stock.objects.filter(remaining_quantity__lt=10)
    context = {
        'low_quantity_stocks': low_quantity_stocks
        }
    return render(request, 'stock_alerts/stockalert.html',context)

def stock(request):
    stock = Stock.objects.all()
    context = {
        'stock': stock
        }
    return render(request, 'stock_management/stock.html',context)
