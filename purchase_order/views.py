from django.forms import ValidationError
from django.shortcuts import render
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



def save_form_data(request):
    if request.method == 'POST':
        supplier =request.POST.get('supplier')
        products = request.POST.getlist('product[]')
        quantities = request.POST.getlist('quantity[]')
        unit_prices = request.POST.getlist('unit_price[]')
        totals = request.POST.getlist('totals[]')
        supplier_obj = Supplier.objects.get(id = supplier)
        # supplier = Supplier.objects.filter(pk = supplier_id)
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
                    supplier_obj = supplier_obj,
                    product_name=product,
                    quantity=quantity,
                    unit_price=unit_price,
                    totals = total
                )
            except ValidationError as e:
                return HttpResponse(f'Error saving product: {e}')

        return HttpResponse('Form data saved successfully.')

    return HttpResponse('Invalid request method.')