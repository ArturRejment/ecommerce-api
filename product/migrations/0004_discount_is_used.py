# Generated by Django 3.2.6 on 2021-12-21 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_stock_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='is_used',
            field=models.BooleanField(default=False, verbose_name='Czy został użyty'),
        ),
    ]