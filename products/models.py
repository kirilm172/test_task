from django.db import models

class Category(models.Model):
    name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(unique=True, max_length=255)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(max_length=255, choices=[('in_stock', 'In stock'), ('out_of_stock', 'Out of stock')])
    remains = models.IntegerField()

    def __str__(self):
        return self.name
