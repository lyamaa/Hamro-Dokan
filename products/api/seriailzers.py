from django.db import models
from django.db.models import fields
from rest_framework import serializers

from ..models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "get_absolute_url", "descritption", "price", "get_image", "get_thumbnail")
