from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    context = {'title': 'Store'}
    return render(request, 'product/index.html',context)

def products(request):
    productcategorie = ProductCategory.objects.all()
    products = Product.objects.all()
    context = {
        'title': 'Store-Каталог',
        'productcategorie': productcategorie,
        'products': products,
    }
    return render(request, 'product/products.html', context)