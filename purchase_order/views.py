from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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