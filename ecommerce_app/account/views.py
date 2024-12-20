from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm  # Import custom form

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Signup successful! You are now logged in.")
            return redirect('home')
        else:
            messages.error(request, "Signup failed. Please check the form for errors.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.error(request, "Login failed. Please check your username and password.")
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')
