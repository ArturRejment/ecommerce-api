# Generated by Django 3.2.6 on 2021-11-22 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, unique=True, verbose_name='Nazwa kategorii')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Opis')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, unique=True, verbose_name='Kod rabatowy')),
                ('percentage_value', models.PositiveIntegerField(verbose_name='Wartość procentowa')),
                ('is_disposable', models.BooleanField(default=True, verbose_name='Czy jednorazowy')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nazwa sezonu')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Opis')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nazwa')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Opis')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255, verbose_name='Nazwa produktu')),
                ('detail_description', models.TextField(blank=True, null=True, verbose_name='Opis')),
                ('stock_status', models.PositiveIntegerField(choices=[(0, 'Brak'), (10, 'Ostatnie sztuki'), (20, 'Dostępne')], verbose_name='Dostępność')),
                ('retail_price_net', models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Detaliczna cena netto [zł]')),
                ('whole_price_whole', models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Hurtowa cena netto [zł]')),
                ('tax', models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Podatek VAT [%]')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Czy widoczny')),
                ('is_new', models.BooleanField(default=True, verbose_name='Czy nowy')),
                ('accession_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Numer katalogowy')),
                ('shipping_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Cena dostawy')),
                ('product_picture', models.ImageField(default='default.jpg', upload_to='product_pictures')),
                ('categories', models.ManyToManyField(related_name='product_category', to='product.Category', verbose_name='Kategorie')),
                ('seasons', models.ManyToManyField(related_name='season_category', to='product.Season', verbose_name='Sezony')),
                ('tags', models.ManyToManyField(related_name='product_tags', to='product.Tag', verbose_name='Tagi')),
            ],
            options={
                'ordering': ('product_name',),
            },
        ),
    ]
