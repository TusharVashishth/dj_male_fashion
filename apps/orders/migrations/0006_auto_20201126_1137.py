# Generated by Django 3.1.3 on 2020-11-26 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20201124_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 26, 11, 37, 45, 183306)),
        ),
    ]
