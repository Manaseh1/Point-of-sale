from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Sales, salesItems
from django.contrib.auth.decorators import login_required

@login_required
def sales_dashboard(request):
    return render(request, 'sales_dashboard.html')
@login_required
def pos(request):
    return render(request, 'pos.html')
