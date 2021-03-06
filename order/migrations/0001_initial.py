# Generated by Django 3.2.6 on 2021-11-22 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost_net', models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Całkowity koszt zamówienia')),
                ('discount_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Kod rabatowy')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Nieopłacone'), (10, 'Opłacone'), (20, 'W realizacji'), (30, 'Wysłane'), (40, 'Gotowe do odbioru'), (50, 'Dostarczone')], default=0, verbose_name='Status')),
                ('cart', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.cart', verbose_name='Koszyk')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik')),
            ],
            options={
                'verbose_name': 'Zamówienie',
                'verbose_name_plural': 'Zamówienia',
            },
        ),
    ]
