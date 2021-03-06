# Generated by Django 3.1.1 on 2020-09-15 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand', '0002_auto_20200915_2216'),
        ('category', '0002_auto_20200915_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('size', models.CharField(max_length=100, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('color', models.CharField(max_length=300, null=True)),
                ('description', models.TextField(max_length=2000, null=True)),
                ('sold', models.IntegerField(default=0, null=True)),
                ('sale', models.IntegerField(choices=[(0, 'no'), (1, 'yes')], default=0, null=True)),
                ('image1', models.ImageField(null=True, upload_to='images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('status', models.IntegerField(choices=[(1, 'active'), (0, 'inactive')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='brand.brand')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
