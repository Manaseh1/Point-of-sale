from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from psycopg2 import IntegrityError
from .models import Sales, salesItems
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import date, datetime
from django.db.models import Sum
from django.utils import timezone

@login_required
def sales_dashboard(request):
    today = datetime.now().date()
    salesc = Sales.objects.filter(date_added__date=today).order_by('-date_added')
    sales = Sales.objects.order_by('-date_added')
    total_sales = salesc.aggregate(total=Sum('grand_total'))['total'] or 0
    return render(request, 'sales_dashboard.html', {'sales': sales, 'total_sales': total_sales})


@login_required
def pos(request):
    products = Product.objects.all()

    if request.method == 'POST':
        try:
            # Save the sale data
            now = datetime.now()
            pref = now.strftime("%Y%m%d%H%M%S")
            i = 1
            while True:
                code = '{:0>5}'.format(i)
                i += 1
                check = Sales.objects.filter(code=str(pref) + str(code)).all()
                if len(check) <= 0:
                    break
            code = str(pref) + str(code)
            grand_total = request.POST.get('grand_total')
            sub_total = request.POST.get('sub_total')
            tax = request.POST.get('tax')
            tax_amount = request.POST.get('tax_amount')
            tendered_amount = request.POST.get('tendered_amount')
            amount_change = request.POST.get('amount_change')

            sale = Sales(
                code=code,
                sub_total=sub_total,
                grand_total=grand_total,
                tax_amount=tax_amount,
                tax=tax,
                tendered_amount=tendered_amount,
                amount_change=amount_change,
                date_added = datetime.now()
            )
            sale.save()

            product_names = request.POST.getlist('product_name[]')
            prices = request.POST.getlist('price[]')
            quantities = request.POST.getlist('qty[]')

            for product_name, price, quantity in zip(product_names, prices, quantities):
                item = salesItems(
                    sale=sale,
                    product=product_name,
                    price=price,
                    qty=quantity,
                    total=float(price) * float(quantity)
                )
                item.save()
            sales = Sales.objects.filter(code=code).first()
            transaction = {}
            for field in Sales._meta.get_fields():
                if field.related_model is None:
                    transaction[field.name] = getattr(sales, field.name)
            if 'tax_amount' in transaction:
                transaction['tax_amount'] = format(float(transaction['tax_amount']))
            ItemList = salesItems.objects.filter(sale_id=sales).all()
            context = {
                "transaction": transaction,
                "salesItems": ItemList
            }

            # Return the template with the saved sale data
            return render(request, 'receipt.html', context)

        except IntegrityError as e:
            error_message = "An error occurred while saving the data. Please try again."
            return render(request, 'pos.html', {'products': products, 'error_message': error_message})

    return render(request, 'pos.html', {'products': products})

def receipt_view(request, sale_id):
    sales = get_object_or_404(Sales, id=sale_id)
    transaction = {}
    for field in Sales._meta.get_fields():
        if field.related_model is None:
            transaction[field.name] = getattr(sales, field.name)
    if 'tax_amount' in transaction:
        transaction['tax_amount'] = format(float(transaction['tax_amount']), '.2f')
    ItemList = salesItems.objects.filter(sale_id=sales)
    context = {
        "transaction": transaction,
        "salesItems": ItemList
    }
    return render(request, 'receipt.html', context)
@login_required
def delete_sale(request, sale_id):
    try:
        sale = Sales.objects.get(id=sale_id)
        sale.delete()
    except Sales.DoesNotExist:
        error_message = "The sale does not exist."
        return render(request, 'sales_dashboard.html', {'error_message': error_message})

    return redirect('sales:sales_dashboard')