from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignupForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)  # Log user in after signup
            return redirect('dashboard')  # Redirect to dashboard
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')

