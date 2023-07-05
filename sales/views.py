from django.shortcuts import render,get_object_or_404
from django.shortcuts import render, redirect
from .models import Sales, salesItems
from inventory.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def sales_dashboard(request):

    return render(request, 'sales_dashboard.html')
@login_required
def pos(request):
    products = Product.objects.all()
    # prod = get_object_or_404(Product,pk=pk)
    # additem, created = salesItems.objects.get_or_create(product = prod)
    # additem.save()
    context = {
        'products': products,
        # 'additem': additem,
    }    
    return render(request, 'pos.html',context)
