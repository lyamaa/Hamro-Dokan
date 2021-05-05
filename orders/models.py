import django
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    first_name = models.CharField(_("First Name"), max_length=255)
    middle_name = models.CharField(_("Middle Name"), max_length=255)
    last_name = models.CharField(_("Last Name"), max_length=255)
    email = models.EmailField(_("Email"), max_length=255)
    address = models.CharField(_("Address"), max_length=255)
    zipcode = models.CharField(_("Zip Code"), max_length=255)
    place = models.CharField(_("Place"), max_length=255)
    phone = models.CharField(_("Phone Number"), max_length=255)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stripe_token = models.CharField(_("Stripe Token"), max_length=255)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.id}"
