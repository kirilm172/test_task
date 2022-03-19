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

        for category in Category.objects.all():
            category.delete()

        for product in Product.objects.all():
            product.delete()

        Category.objects.bulk_create([Category(name=f'category{i + 1}') for i in range(cc)])

        for i, category in enumerate(Category.objects.all()):
            Product.objects.bulk_create([Product(
                name=f'product{(i + 1)*pc + j}',
                category = category,
                price = random.randint(0, 10000)/100,
                status = random.choice(['in_stock', 'out_of_stock']),
                remains = random.randint(0, 100)
            ) for j in range(pc)])