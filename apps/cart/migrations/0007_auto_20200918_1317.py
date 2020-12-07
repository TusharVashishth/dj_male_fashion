# Generated by Django 3.1.1 on 2020-09-18 07:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20200918_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 18, 13, 17, 47, 88352)),
        ),
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.IntegerField(choices=[(0, 'cart'), (1, 'buy')], default=0),
        ),
    ]