from django.urls import include, path

from .views import LatestProductList, ProductDetail

urlpatterns = [
    path("latest-products/", LatestProductList.as_view()),
    path("product/<slug:category_slug>/<slug:product_slug>/", ProductDetail.as_view()),
]
