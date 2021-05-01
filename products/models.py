from io import BytesIO

from django.core.files import File
from django.db import models
from django.db.models.expressions import OrderBy
from django.utils.translation import gettext_lazy as _
from PIL import Image


class Category(models.Model):
    name = models.CharField(_("Category Name"), max_length=50)
    slug = models.SlugField(_("Category Slug"), unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f"/{self.slug}/"


class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(_("Product Name"), max_length=50)
    slug = models.SlugField(_("Product Slug"), unique=True)
    descritption = models.TextField(_("Product Description"))
    price = models.DecimalField(_("Product PRice"), max_digits=6, decimal_places=2)
    image = models.ImageField(_("Product Image"), upload_to="product/", blank=True, null=True)
    thumbnail = models.ImageField(_("Product Thumbnail"), upload_to="product/thumbnail/", blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date_added",)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f"/{self.category.slug}/{self.slug}/"

    def get_image(self):
        if self.image:
            return "http://127.0.0.1:8000" + self.image.url
        return ""

    def get_thumbnail(self):
        if self.thumbnail:
            return "http://127.0.0.1:8000" + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return "http://127.0.0.1:8000" + self.thumbnail.url
            else:
                return ""

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, "jpeg", quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
