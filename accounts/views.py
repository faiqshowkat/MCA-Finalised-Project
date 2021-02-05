
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup-login.html', {'error': 'username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('homepage')
        else:
            return render(request, 'accounts/signup-login.html', {'error': 'Passwords must match'})
    else:
        return render(request, 'accounts/signup-login.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'accounts/signup-login.html', {'error': 'username or password incorrect'})
    else:
        return render(request, 'accounts/signup-login.html')


def logout(request):
    return render(request, 'accounts/logout.html')
