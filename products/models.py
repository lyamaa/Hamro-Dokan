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
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f"/{self.slug}/"


class ProductType(models.Model):
    name = models.CharField(_("Product Type"), max_length=255)
    is_active = models.BooleanField(_("Is Active"), default=True)

    class Meta:
        verbose_name = _("Product Type")
        verbose_name_plural = _("Product Types")

    def __str__(self) -> str:
        return self.name


class ProductSpecs(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    name = models.CharField(_("Name"), max_length=255)

    class Meta:
        verbose_name = _("Product Specification")
        verbose_name_plural = _("Product Specifications")

    def __str__(self):
        return self.name


class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.RESTRICT)
    name = models.CharField(_("Product Name"), max_length=50)
    slug = models.SlugField(_("Product Slug"), unique=True)
    description = models.TextField()
    price = models.DecimalField(_("Product Price"), max_digits=6, decimal_places=2)
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
        return f"http://127.0.0.1:8000{self.image.url}" if self.image else ""

    def get_thumbnail(self):
        if self.thumbnail:
            return f"http://127.0.0.1:8000{self.thumbnail.url}"
        if self.image:
            self.thumbnail = self.make_thumbnail(self.image)
            self.save()
            return f"http://127.0.0.1:8000{self.thumbnail.url}"
        else:
            return ""

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, "jpeg", quality=85)

        return File(thumb_io, name=image.name)


class ProductSpecificationValue(models.Model):
    """
    The Product Specification Value table holds each of the
    products individual specification or features.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(ProductSpecs, on_delete=models.RESTRICT)
    value = models.CharField(
        verbose_name=_("value"),
        help_text=_("Product specification value (maximum of 255 words"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Product Specification Value")
        verbose_name_plural = _("Product Specification Values")

    def __str__(self):
        return self.value


class ProductImage(models.Model):
    """
    The Product Image table.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")
    images = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Upload a product image"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=_("Alturnative text"),
        help_text=_("Please add alturnative text"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")

    def get_images(self):
        return f"http://127.0.0.1:8000{self.images.url}" if self.image else ""
