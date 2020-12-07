from django.db import models
from utils.choices import status_choice


class Brand(models.Model):
    name = models.CharField(max_length=200, null=True)
    status = models.IntegerField(choices=status_choice(), default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
