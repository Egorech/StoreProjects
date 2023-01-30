from django.urls import path
from .views import *



urlpatterns = [path('', IndexView.as_view(), name = 'index'),
               path('products/', ProductsListView.as_view(), name = 'products'),
               path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
               path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),
               path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
               path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
               ]