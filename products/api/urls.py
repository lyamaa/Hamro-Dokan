from django.urls import include, path

from .views import (
    CategoryDetail,
    LatestProductList,
    ProductDetail,
    SearchProductList,
    search,
)

urlpatterns = [
    path("latest-products/", LatestProductList.as_view()),
    path("product/<slug:category_slug>/<slug:product_slug>/", ProductDetail.as_view()),
    path("products/<slug:category_slug>/", CategoryDetail.as_view()),
    path("products/search", search),
]
