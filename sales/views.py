from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from psycopg2 import IntegrityError
from .models import Sales, salesItems, MoneyControl
from inventory.models import Product
from stockmgt.models import Stock
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
    Mpesa = MoneyControl.objects.filter(payment_method = "Mpesa")
    Cash = MoneyControl.objects.filter(payment_method = "Cash")
    totalMpesa = Mpesa.aggregate(total=Sum('Amount'))['total'] or 0
    totalCash = Cash.aggregate(total=Sum('Amount'))['total'] or 0
    total_sales = salesc.aggregate(total=Sum('grand_total'))['total'] or 0
    context = {
        'sales': sales, 
        'total_sales': total_sales,
        'totalMpesa': totalMpesa,
        'totalCash': totalCash
        }
    return render(request, 'sales_dashboard.html', context)


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
            prodIds=request.POST.getlist('product_id[]')

            for product_name, price, quantity,product_id in zip(product_names, prices, quantities,prodIds):
                item = salesItems(
                    sale=sale,
                    product=product_name,
                    price=price,
                    qty=quantity,
                    total=float(price) * float(quantity)
                    
                )
                item.save()
                stock = Stock.objects.filter(product=product_id).first()
                if stock:
                    stock.remaining_quantity -= int(quantity)
                    stock.save()
            mpesa = request.POST.get('mpesa')
            tcash = request.POST.get('cash')
            cash = float(tcash) - float(amount_change)

            if float(mpesa) > 0:
                mpesa_moneycontrol = MoneyControl(sale=sale, payment_method='Mpesa', Amount=float(mpesa))
                mpesa_moneycontrol.save()

            if float(cash) > 0:
                cash_moneycontrol = MoneyControl(sale=sale, payment_method='Cash', Amount=float(cash))
                cash_moneycontrol.save()

            sales = Sales.objects.filter(code=code).first()
            transaction = {}
            for field in Sales._meta.get_fields():
                if field.related_model is None:
                    transaction[field.name] = getattr(sales, field.name)
            if 'tax_amount' in transaction:
                transaction['tax_amount'] = format(float(transaction['tax_amount']))
            ItemList = salesItems.objects.filter(sale_id=sales).all()
            payment_method  = MoneyControl.objects.filter(sale_id=sales).all()
            context = {
                "transaction": transaction,
                "salesItems": ItemList,
                "payment_method":payment_method
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
    payment_method  = MoneyControl.objects.filter(sale_id=sales).all()
    context = {
        "transaction": transaction,
        "salesItems": ItemList,
        "payment_method":payment_method
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