from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Product
from .seriailzers import ProductSerializer


class LatestProductList(APIView):
    def get(self, requet, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)
