from django.shortcuts import render, HttpResponseRedirect
from .models import *
from users.models import User
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

def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])