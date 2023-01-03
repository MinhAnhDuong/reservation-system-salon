from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "OK")
        messages.error(request, "NOT OK")
    else:
        form = RegisterForm()
    return render(request=request, template_name="user/register.html", context={"register_form":form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are logged in.")
                return redirect('/beauty-salon/reservation/reservationslist/')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request=request, template_name="user/login.html", context={'login_form':form})

def logout_user(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('/beauty-salon/')