from django.shortcuts import render
from  users.models import User
from  users.forms import UserLoginForm
# Create your views here.

def login(request):
    context = {'form': UserLoginForm()}
    return render(request, 'users/login.html', context)

def register(request):
    return render(request, 'users/register.html')