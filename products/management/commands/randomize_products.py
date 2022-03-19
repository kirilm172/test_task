from django.core.management.base import BaseCommand
from products.models import Product

import random

class Command(BaseCommand):
    help = 'Randomize products'

    def handle(self, *args, **kwargs):

        for product in Product.objects.all():
            product.price = random.randint(0, 10000)/100
            product.status = random.choice(['in_stock', 'out_of_stock'])
            product.remains = random.randint(0, 100)
            product.save()