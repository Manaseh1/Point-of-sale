from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.contrib.sites.shortcuts import get_current_site
from .forms import *
from django.contrib import messages
# Create your views here.
def home(request):
    form = SignupForm()
    if request.method == 'POST':  
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username exists")
        email = request.POST['email']            
        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email exists")
        if request.POST['password1'] !=request.POST['password2']:
            messages.warning(request,"passwords do not match") 
        form = SignupForm(request.POST)

        if form.is_valid(): 
             
            form.save()
            messages.success(request,"Successful Signup. LOGIN!") 
            return redirect('accounts:login')

    return render(request,'home.html',{'form':form})

def signin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username =cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('dashboard:index')
                else:
                    messages.warning(request,'Login failed')    
            else:
                messages.warning(request,'Login failed')    
    return render(request,'login.html',{'form':form})
