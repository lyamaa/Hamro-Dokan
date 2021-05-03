from django.contrib import admin

from .models import (
    Category,
    Product,
    ProductSpecificationValue,
    ProductSpecs,
    ProductType,
)

admin.site.register(Category)


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecs


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationInline,
    ]


class ProductSpecificationValueInline(admin.TabularInline):
    model = ProductSpecificationValue


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationValueInline,
    ]
