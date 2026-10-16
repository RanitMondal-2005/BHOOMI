# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import authenticate
from .forms import StyledLoginForm

# ----------- New User Registration ------------------------------
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully.')
            return redirect('landing_page')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


# -------- Custom Login/Logout Views with default login/logout() functions ---------------

# logout view
def logout_view(request):
    messages.success(request, 'You have been logged out successfully.')
    logout(request)
    return redirect('landing_page')

# login view
def login_view(request):
    if request.method == 'POST':
        form = StyledLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('landing_page')
    else:
        form = StyledLoginForm()

    return render(request, 'accounts/login.html', {'form': form})
