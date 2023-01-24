from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'title': 'Test Title',
               'username': 'Valeria'
    }
    return render(request, 'product/index.html',context)

def products(request):
    return render(request, 'product/products.html')