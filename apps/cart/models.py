from django.db import models
from apps.product.models import Product
from django.contrib.auth.models import User
from datetime import datetime
from utils.choices import cart_choices


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(choices=cart_choices(), default=0)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.product.name

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
