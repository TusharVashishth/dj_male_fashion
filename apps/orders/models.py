from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from apps.product.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    quantity = models.CharField(max_length=200, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    transaction_id = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
