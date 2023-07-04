from django.shortcuts import render,redirect
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import CreateProductForm,SupplierForm,CategoryForm,EditProductForm
from .models import *
# @login_required(login_url='login')
def inventory_dashboard(request):
    products = Product.objects.all()
    current_site = get_current_site(request)
    supplier_count = Supplier.objects.count()
    category_count = Category.objects.count()
    context = {
        'products': products,
        'current_site': current_site,
        'supplier_count': supplier_count,
        'category_count': category_count
    }

    return render(request, 'inventory_dashboard.html', context)

class CreateProduct(CreateView):
    template_name = 'product/prodadd.html'
    form_class = CreateProductForm
    model = Product
    success_url ='Inventory_Dasboard/'

class EditProduct(UpdateView):
    template_name = 'product/editproduct.html'
    form_class = EditProductForm
    model = Product
    def get_success_url(self):
        # Custom logic to determine the success URL
        # For example, redirecting to the inventory dashboard
        return reverse_lazy('inventory:inventory_dashboard')


class DeleteProduct(DeleteView):
    template_name = 'product/deleteproduct.html'
    model = Product
    success_url ='Inventory_Dasboard/'


def create_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'supplier/create_supplier.html', {'form': form})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:category_list')
    else:
        form = CategoryForm()
    return render(request, 'category/create_category.html', {'form': form})

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier/supplier_list.html', {'suppliers': suppliers})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})

def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('inventory:category_list')

def delete_supplier(request, supplier_id):
    supplier = Supplier.objects.get(id=supplier_id)
    supplier.delete()
    return redirect('inventory:supplier_list')