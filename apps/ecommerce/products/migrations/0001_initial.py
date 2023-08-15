# Generated by Django 4.2.4 on 2023-08-12 12:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('color', 'Color'), ('size', 'Size'), ('weight', 'Weight'), ('count', 'Count')], max_length=50, verbose_name='Attribute type')),
                ('name', models.CharField(help_text='Required. 50 characters or fewer.', max_length=50, unique=True, verbose_name='Attribute name')),
            ],
            options={
                'verbose_name_plural': 'Product attributes',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Required. 50 characters or fewer.', max_length=50, unique=True, verbose_name='Brand name')),
                ('slug', models.SlugField(blank=True, help_text='Generated automatically on save.', max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Brands',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required. 100 characters or fewer.', max_length=100, unique=True, verbose_name='Category name')),
                ('slug', models.SlugField(blank=True, help_text='Generated automatically on save.', max_length=150, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last updated')),
                ('sku', models.CharField(blank=True, help_text='Generated automatically on save.', max_length=15, unique=True)),
                ('slug', models.SlugField(blank=True, help_text='Generated automatically on save.', max_length=200, unique=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('name', models.CharField(help_text='Required. 150 characters or fewer.', max_length=150, unique=True, verbose_name='Product name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_reviewed', models.BooleanField(default=False, verbose_name='Reviewed')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('attributes', models.ManyToManyField(blank=True, related_name='product_attributes', to='products.attribute')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_brand', to='products.brand')),
                ('category', models.ManyToManyField(blank=True, related_name='product_category', to='products.category')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last updated')),
                ('sku', models.CharField(blank=True, help_text='Generated automatically on save.', max_length=15, unique=True)),
                ('slug', models.SlugField(blank=True, help_text='Generated automatically on save.', max_length=200, unique=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('name', models.CharField(help_text='Required. 150 characters or fewer.', max_length=150, unique=True, verbose_name='Product name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_reviewed', models.BooleanField(default=False, verbose_name='Reviewed')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('attributes', models.ManyToManyField(blank=True, related_name='variant_attributes', to='products.attribute')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='products.product')),
            ],
            options={
                'verbose_name_plural': 'Product Variants',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='KeyBenefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='key_benefits', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('alt_text', models.CharField(blank=True, max_length=200, null=True)),
                ('img_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product')),
                ('variant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.variant')),
            ],
        ),
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='benefits', to='products.product')),
            ],
        ),
    ]