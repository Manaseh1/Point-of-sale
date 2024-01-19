from django.shortcuts import render,redirect
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from accommodation.views import *
@login_required(login_url='login')
def CustomersMgtDashboard(request):
    customers = Customer.objects.all()
    
    context = {
        'customers': customers
        }
    
    return render(request, 'customers.html', context)
@login_required(login_url='login')
def underdev(request):
    
    context = {

    }
    return render(request, 'underdev.html', context)
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html')
def add_customer(request):
    if request.method == 'POST':
        form = EditCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accommodation:customer_list')
    else:
        form = EditCustomerForm()
    return render(request, 'customers/add_customer.html', {'form': form})

# View to edit an existing customer
def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        form = EditCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('accommodation:customer_list')
    else:
        form = EditCustomerForm(instance=customer)
    return render(request, 'customers/edit_customer.html', {'form': form, 'customer': customer})

def delete_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        room.delete()
        return redirect('accommodation:room_list')
    return JsonResponse({'success': False})


