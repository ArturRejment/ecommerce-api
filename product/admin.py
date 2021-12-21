from django.contrib import admin
from .models import (
    Product, Category, Season, Tag, Discount,
)

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Season)
admin.site.register(Tag)
admin.site.register(Discount)
