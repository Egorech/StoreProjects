from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from  users.models import User
from  users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
# Create your views here.
from django.contrib import auth, messages

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Welcome!!!!')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance = request.user, data = request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = UserProfileForm(instance = request.user)
    context = {'title': 'Профиль',
               'form': form,
               }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))