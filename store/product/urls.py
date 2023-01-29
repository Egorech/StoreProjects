from django.urls import path
from .views import *



urlpatterns = [path('', index, name = 'index'),
               path('products/', products, name = 'products'),
               path('category/<int:category_id>/', products, name='category'),
               path('page/<int:page_number>/', products, name='paginator'),
               path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
               path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
               ]