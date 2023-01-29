from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from .models import *
from django.core.paginator import Paginator

# Create your views here.

class IndexView(TemplateView):
    template_name = 'product/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Store'
        return context


class ProductsListView(ListView):
    model = Product
    template_name = 'product/products.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['title'] = 'Store-Каталог'
        context['productcategorie'] = ProductCategory.objects.all()
        return context

def products(request, category_id=None, page_number=1):
    if category_id:
        category = ProductCategory.objects.get(id=category_id)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    paginator = Paginator(object_list = products, per_page = 3)
    products_paginator = paginator.page(page_number)

    context = {
        'title': 'Store-Каталог',
        'productcategorie': ProductCategory.objects.all(),
        'products': products_paginator,
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