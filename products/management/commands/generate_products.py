from itertools import product
from django.core.management.base import BaseCommand
from products.models import Category, Product
import random

class Command(BaseCommand):
    help = 'Generate random products'

    def add_arguments(self, parser):
        parser.add_argument('cc', type=int, help='Categories count')
        parser.add_argument('pc', type=int, help='Products count')

    def handle(self, *args, **kwargs):
        cc = kwargs['cc']
        pc = kwargs['pc']

        Category.objects.all().delete()
        Product.objects.all().delete()

        categories = Category.objects.bulk_create([Category(name=f'category{i + 1}') for i in range(cc)])

        products_to_create = []
        for i, category in enumerate(categories):
            for j in range(pc):
                product = Product(
                    name=f'product{(i + 1)*pc + j}',
                    category = category,
                    price = random.randint(0, 10000)/100,
                    status = random.choice(['in_stock', 'out_of_stock']),
                    remains = random.randint(0, 100)
                )
                products_to_create.append(product)
        Product.objects.bulk_create(products_to_create)