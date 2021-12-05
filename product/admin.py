from django.contrib import admin
from .models import (
    Product, Category, Season, Tag,
)

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Season)
admin.site.register(Tag)
