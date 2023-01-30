from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, CreateView
from .models import *
from common.views import TitleMixin

# Create your views here.

class IndexView(TitleMixin, TemplateView):
    template_name = 'product/index.html'
    title = 'Store'


class ProductsListView(TitleMixin, ListView):
    model = Product
    template_name = 'product/products.html'
    paginate_by = 3
    title = 'Store-Каталог'

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['productcategorie'] = ProductCategory.objects.all()
        return context


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