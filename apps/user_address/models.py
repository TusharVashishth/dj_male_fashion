from django.db import models
from datetime import datetime
from utils.choices import status_choice
from django.contrib.auth.models import User
from django.core import validators


class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True , blank=True)
    street_address = models.CharField(max_length=500, null=True, validators=[validators.MinLengthValidator(5)])
    apartment = models.CharField(max_length=500, null=True, validators=[validators.MinLengthValidator(5)])
    city = models.CharField(max_length=500, null=True, validators=[validators.MinLengthValidator(2)])
    state = models.CharField(max_length=300, null=True, validators=[validators.MinLengthValidator(5)])
    pincode = models.CharField(max_length=50, null=True,
                               validators=[validators.MinLengthValidator(6), validators.MaxLengthValidator(6)])
    phone_no = models.CharField(max_length=15 , null=True,
                                   validators=[validators.MinLengthValidator(10) , validators.MaxLengthValidator(11)])
    status = models.IntegerField(choices=status_choice(), default=1)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
