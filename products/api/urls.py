from django.urls import include, path

from .views import LatestProductList

urlpatterns = [path("latest-products/", LatestProductList.as_view())]
