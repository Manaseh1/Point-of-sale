from django.shortcuts import render,get_object_or_404
from django.shortcuts import render, redirect
from .models import Sales, salesItems
from inventory.models import Product
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def sales_dashboard(request):

    return render(request, 'sales_dashboard.html')
@login_required
def pos(request):
    products = Product.objects.all()
    sales = Sales.objects.all()
    salesitems = salesItems.objects.all()
    context = {
        'products': products,
        'sales': sales,
        'salesitems': salesitems
    }
    return render(request, 'pos.html', context)
