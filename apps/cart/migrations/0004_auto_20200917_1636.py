# Generated by Django 3.1.1 on 2020-09-17 11:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20200917_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 17, 16, 36, 32, 744284)),
        ),
    ]