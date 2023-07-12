from django.forms import ValidationError
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Purchase
from inventory.models import Supplier

from .forms import order_form
# Create your views here.
@login_required
def purchase_order(request):
    form = order_form()
    if form.is_valid():
        form = order_form(request.POST)
    context ={
        'form':form
    }
    return render(request,'purchase_order.html',context)

@login_required
def purchase_items(request):
    purchases = Purchase.objects.all()
    context  = {
        'purchases': purchases
    }
    return render(request,'purchases_items.html',context)

def save_form_data(request):
    if request.method == 'POST':
        supplier = request.POST.get('supplier')
        products = request.POST.getlist('product[]')
        quantities = request.POST.getlist('quantity[]')
        unit_prices = request.POST.getlist('unit_price[]')
        totals = request.POST.getlist('totals[]')
        supplier_obj = Supplier.objects.get(pk=supplier)
        for product, quantity, unit_price,total in zip(products, quantities, unit_prices,totals):
            if not quantity:
                return HttpResponse('Quantity field cannot be empty.')

            try:
                quantity = int(quantity)
            except ValueError:
                return HttpResponse('Invalid quantity value.')

            try:
                unit_price = float(unit_price)
            except ValueError:
                return HttpResponse('Invalid unit price value.')

            # Create a new Product object and save it to the database
            try:
                Purchase.objects.create(
                    supplier = supplier_obj,
                    product_name=product,
                    quantity=quantity,
                    unit_price=unit_price,
                    totals = total
                )
            except ValidationError as e:
                return HttpResponse(f'Error saving product: {e}')

        return redirect('purchase:purchase_items')

    return HttpResponse('Invalid request method.')