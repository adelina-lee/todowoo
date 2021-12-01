from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, \
    AuthenticationForm  # Import user creation form & user creation form
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, 'todo/home.html')


def register(request):
    if request.method == 'GET':
        return render(request,
                      'todo/register.html',
                      {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Create a new user
                user = User.objects.create_user(
                    request.POST['username'],  # Username
                    password=request.POST['password1'])  # Password
                user.save()  # Save into db
                login(request, user)  # Login user
                return redirect('current')  # Redirect user to current page
            except IntegrityError:
                return render(request,
                              'todo/register.html',
                              {'form': UserCreationForm(),
                               'error': 'The username you chose has already been taken. Choose a new username.'})
        else:
            # Tell user that passwords didn't match
            return render(request,
                          'todo/register.html',
                          {'form': UserCreationForm(),
                           'error': 'Passwords did not match.'})


def loginuser(request):
    if request.method == 'GET':
        return render(request,
                      'todo/loginuser.html',
                      {'form': AuthenticationForm()})
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request,
                          'todo/loginuser.html',
                          {'form': AuthenticationForm(),
                           'error': 'Username and password did not match.'})
        else:
            login(request, user)  # Login user
            return redirect('current')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def current(request):
    return render(request, 'todo/current.html')
