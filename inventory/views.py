from django.shortcuts import render,redirect
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from .forms import CreateProductForm
from .models import Product
# @login_required(login_url='login')
def inventory_dashboard(request):
    products = Product.objects.all()
    current_site = get_current_site(request)
    context = {
        'products':products,
        'current_site': current_site,
    }

    return render(request, 'inventory_dashboard.html', context)

class CreateProduct(CreateView):
    template_name = 'prodadd.html'
    form_class = CreateProductForm
    model = Product
    success_url ='Inventory_Dasboard/'
