from django.forms import ValidationError
from django.shortcuts import get_object_or_404, render

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Purchase,Order
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
        order =request.POST.get('order')
        supplier =request.POST.get('supplier')
        products = request.POST.getlist('product[]')
        quantities = request.POST.getlist('quantity[]')
        unit_prices = request.POST.getlist('unit_price[]')
        totals = request.POST.getlist('totals[]')
        supplier_obj = Supplier.objects.get(pk=supplier)
        supplier_email = Supplier.objects.values('email').get(pk=supplier)
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
                new_order = Order.objects.create(
                    order_name = order   
                )
                
                Purchase.objects.create(
                    order = new_order, 
                    supplier = supplier_obj,
                    email = supplier_email['email'],
                    product_name=product,
                    quantity=quantity,
                    unit_price=unit_price,
                    totals = total
                )
            except ValidationError as e:
                return HttpResponse(f'Error saving product: {e}')

        return redirect('purchase:purchase_items')

    return HttpResponse('Invalid request method.')

from django.shortcuts import render, get_object_or_404
from .models import Purchase  # Import your Purchase model (adjust the import path as needed)

def receipt(request, purchase_id):
    # Assuming purchase_id is passed as a parameter to this view function.

    # Retrieve the Purchase object or raise a 404 error if it doesn't exist
    purchase = get_object_or_404(Purchase, order=purchase_id)

    # Create lists containing the values for each field
    products = list(Purchase.objects.filter(order=purchase_id).values_list('product_name', flat=True))
    quantities = list(Purchase.objects.filter(order=purchase_id).values_list('quantity', flat=True))
    totals = list(Purchase.objects.filter(order=purchase_id).values_list('totals', flat=True))

    # Zip the lists together to create a list of tuples, each containing the values for one entry
    receipt_items = zip(products, quantities, totals)

    context = {
        'receipt_items': receipt_items,
    }

    return render(request, 'receipts.html', context)

# def receipt(request,purchase_id):
#     # purchase_items = get_object_or_404(Purchase,order = purchase_id)
#     product = Purchase.objects.values_list('product_name', flat=True).filter(order=purchase_id)
#     # product = product.get('product_name')
#     product = product[0]    
#     quantity = Purchase.objects.values_list('quantity',flat=True).filter(order = purchase_id)
#     quantity = quantity[0]
#     totals = Purchase.objects.values_list('totals',flat=True).filter(order = purchase_id)
#     totals = totals[0]
    
#     context ={
#         # 'purchase_items':purchase_items,
#         'quantity':quantity,
#         'totals':totals,
#         'product':product
        
#     }
#     return render(request,'receipts.html',context)