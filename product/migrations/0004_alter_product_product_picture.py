# Generated by Django 3.2.6 on 2021-08-16 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_picture',
            field=models.ImageField(default='default.jpg', upload_to='product_pictures'),
        ),
    ]