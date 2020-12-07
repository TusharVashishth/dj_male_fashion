from django.db import models
from apps.brand.models import Brand
from apps.category.models import Category
from utils.choices import sale_choices, status_choice
from django.utils.safestring import mark_safe


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    brand = models.ForeignKey(Brand, models.CASCADE, null=True)
    category = models.ForeignKey(Category, models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.IntegerField(null=True)
    color = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True)
    sold = models.IntegerField(null=True, default=0)
    sale = models.IntegerField(choices=sale_choices(), null=True, default=0)
    image1 = models.ImageField(upload_to='images/', null=True)
    image2 = models.ImageField(upload_to='images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='images/', null=True, blank=True)
    status = models.IntegerField(choices=status_choice(), default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image1.url))

    image_tag.short_description = 'Images'
    image_tag.allow_tags = True

    image_tag.short_description = 'image'
    image_tag.allow_tags = True
