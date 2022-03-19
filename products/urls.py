from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('', cache_page(60*5)(views.ProductList.as_view()), name='product_list'),
    path('data', views.ProductData, name='product_data')
]