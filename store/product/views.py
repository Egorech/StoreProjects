from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from users.models import User
# Create your views here.

def index(request):
    context = {'title': 'Store'}
    return render(request, 'product/index.html',context)

def products(request, category_id=None):
    if category_id:
        category = ProductCategory.objects.get(id=category_id)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    productcategorie = ProductCategory.objects.all()
    context = {
        'title': 'Store-Каталог',
        'productcategorie': ProductCategory.objects.all(),
        'products': products,
    }
    return render(request, 'product/products.html', context)

@login_required
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

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])