# Generated by Django 3.1.1 on 2020-09-19 08:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_address', '0005_auto_20200919_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 19, 13, 32, 34, 64062)),
        ),
    ]
