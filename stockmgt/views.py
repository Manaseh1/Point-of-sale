from pyexpat.errors import messages
from inventory.models import Product
from .models import *
from django.shortcuts import render, get_object_or_404,redirect

def restock(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)
    # product 

    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        
        # # Perform validation on the quantity
        # if not quantity:
        #     messages.error(request, 'Quantity field cannot be empty.')
        # elif int(quantity) <= 0:
        #     messages.error(request, 'Quantity must be greater than zero.')
        # else:
        # Update the stock quantity
        stock.remaining_quantity += int(quantity)
        stock.save()
    
        # Redirect to a success page or any other desired view
        return redirect('stock:stock')

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
