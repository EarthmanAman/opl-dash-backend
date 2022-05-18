import datetime

from django.db.models import F, FloatField, Sum
from rest_framework.generics import (
    ListAPIView,
)
from rest_framework.response import Response
from rest_framework import status

from . models import Product
from . serializers import (
    RetrieveProductSer,
    ProductMonthSer, 
    ProductSeriesSer, 
    ProductTopCustomerMonthSer,
)

class ProductListView(ListAPIView):
    serializer_class = RetrieveProductSer
    queryset = Product.objects.all()
    
class ProductSeriesView(ListAPIView):
    serializer_class = ProductSeriesSer
    queryset = Product.objects.all()

class ProductMonthView(ListAPIView):
    serializer_class = ProductMonthSer
    queryset = Product.objects.all()

class ProductTopCustomerMonthView(ListAPIView):
    serializer_class = ProductTopCustomerMonthSer
    queryset = Product.objects.all().prefetch_related("sale_set")