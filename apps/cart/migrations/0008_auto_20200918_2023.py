# Generated by Django 3.1.1 on 2020-09-18 14:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_auto_20200918_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 18, 20, 23, 58, 454244)),
        ),
    ]
