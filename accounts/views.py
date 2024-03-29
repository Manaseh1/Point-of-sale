from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.contrib.sites.shortcuts import get_current_site
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import NewEmployee,Profile
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('oldPassword')
        new_password = request.POST.get('newPassword')
        confirm_password = request.POST.get('confirmPassword')

        # Perform your password change logic here
        # For example, you can use the built-in `set_password` method of the User model
        if request.user.check_password(current_password):
            if new_password == confirm_password:
                request.user.set_password(new_password)
                request.user.save()
                messages.success(request, 'Password changed successfully.')
                return JsonResponse({'success': True})
            else:
                messages.error(request, 'New password and confirm password do not match.')
        else:
            messages.error(request, 'Current password is incorrect.')

    return JsonResponse({'success': False})

# Create your views here.
def home(request):
    form = SignupForm()
    if request.method == 'POST':  
        username = request.POST['username']
        if NewEmployee.objects.filter(username=username).exists():
            messages.warning(request, "Username exists")
        email = request.POST['email']            
        if NewEmployee.objects.filter(email=email).exists():
            messages.warning(request, "Email exists")
        if request.POST['password1'] !=request.POST['password2']:
            messages.warning(request,"passwords do not match") 
        form = SignupForm(request.POST) # type: ignore

        if form.is_valid(): 
             
            form.save()
            print(profile)
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
                    request.session['username'] = cd['username']
                    login(request,user)
                    return redirect('dashboard:index')
                else:
                    messages.warning(request,'Login failed')    
            else:
                messages.warning(request,'Login failed')    
    return render(request,'login.html',{'form':form})

@login_required
def profile(request):
    employee = NewEmployee.objects.get(username =request.user.username)
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        full_name = f"{request.POST.get('first_name')} {request.POST.get('last_name')}"
        city = request.POST.get('city')
        profile_image = request.FILES.get('profile-user-img')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        # role = request.POST.get('role')
        pnonenumber = request.POST.get('phone_number')

        # Retrieve the user
        user = request.user

        # Update the user's profile fields
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.profile.first_name = first_name
        user.profile.last_name = last_name
        user.profile.full_name = full_name
        user.profile.address = address
        user.profile.city = city
        user.profile.profile_image = profile_image
        user.profile.date_of_birth = date_of_birth
        user.profile.gender = gender
        user.profile.date_started = datetime.now()
        user.profile.phone_number = pnonenumber

        # Save the changes
        user.save()
        user.profile.save()
        messages.success(request, 'Profile updated successfully')
        return redirect('accounts:profile')

        # Redirect to a success page or display a success message
    return render(request, 'Profile.html',{'employee':employee})


def session_retrieval_view(request):
    # Get the 'next' parameter from the URL
    username = request.session.get('username')
    next_url = request.GET.get('next')
    user = NewEmployee.objects.get(username=username)
    profile = Profile.objects.get(user__username=username)
    if request.method == 'POST':
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)
        if user is not None:
            # Password is correct
            login(request, user)
            return redirect(next_url) if next_url else redirect('dashboard:index')
        else:
            message = "wrong Password"
            context = {
            'next_url': next_url,
            'username': username,
            'profile': profile,
            'msg': message
            }
            return render(request, 'session_retrieval.html', context)
    context = {
        'next_url': next_url,
        'username': username,
        'profile': profile,
    }
    return render(request, 'session_retrieval.html', context)
