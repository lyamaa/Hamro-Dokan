from django.contrib import admin

from .models import Category, Product

admin.site.register([Product, Category])
