
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import auth


# Create your views here.


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if password1 != password2:
            error = "Your Passwords Didn't Match"
            return render(request, 'accounts/signup-login.html', {'error': error})
        count1 = 0
        count2 = 0
        count3 = 0

        for i in password1:
            if i > "0" and i < '9':
                count1 = 1
            if i > "A" and i < 'Z':
                count2 = 1
            if i > "a" and i < 'z':
                count3 = 1

        if count1 == 0 or count2 == 0 or count3 == 0:
            error = "Your Password is not Strong"
            return render(request, 'accounts/signup-login.html', {'error': error})
        if len(password1) < 8:
            error = "Password Must be 8 Characters"
            return render(request, 'accounts/signup-login.html', {'error': error})
        if len(User.objects.filter(username=username)) == 1:
            error = "Username already exists."
            return render(request, 'accounts/signup-login.html', {'error': error})
        if len(User.objects.filter(email=email)) == 0:
            user = User.objects.create_user(
                username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
            auth.login(request, user)
            return redirect('homepage')
        else:
            error = "Email already exists."
            return render(request, 'accounts/signup-login.html', {'error': error})
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


def logoutuser(request):
    logout(request)
    return redirect('frontpage')
