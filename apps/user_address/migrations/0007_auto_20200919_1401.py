# Generated by Django 3.1.1 on 2020-09-19 08:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_address', '0006_auto_20200919_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 19, 14, 1, 27, 23317)),
        ),
    ]
