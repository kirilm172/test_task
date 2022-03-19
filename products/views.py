from statistics import mode
from time import sleep
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.forms import model_to_dict
import json

from .models import Category, Product

COUNT_BY_PAGE = 50

def ProductData(request):
    page_number = request.GET.get('page', 1)
    cur_category = request.GET.get("category", None)
    if cur_category == 'None':
        cur_category = None

    if cur_category:
        category = get_object_or_404(Category, name=cur_category)
        products = Product.objects.filter(category=category).order_by('name')
    else:
        products = Product.objects.all().order_by('name')

    products = Paginator(products, COUNT_BY_PAGE).get_page(page_number).object_list

    data = []
    for product in products:
        model = model_to_dict(product)
        del model['name'], model['category']
        data.append(model)

    return JsonResponse(data, safe=False)

class ProductList(ListView):
    model = Product
    paginate_by = COUNT_BY_PAGE
    template_name = 'product_list.html'

    def get_queryset(self):
        self.cur_category = self.request.GET.get("category", None)
        if self.cur_category:
            self.category = get_object_or_404(Category, name=self.cur_category)
            return Product.objects.filter(category=self.category).order_by('name')
        else:
            return Product.objects.all().order_by('name')
    
    def get_context_data(self, **kwargs):
        sleep(2)
        context = super(ProductList, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['cur_category'] = self.cur_category
        return context