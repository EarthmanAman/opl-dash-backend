import datetime

from django.db.models import F, FloatField, Sum
from rest_framework.generics import (
    ListAPIView,
)
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import (
    RetrieveProductSer,
    ProductMonthSer,
    ProductSeriesSer,
    ProductTopCustomerMonthSer,
    ProductDepotMonthSer,
)


class ProductListView(ListAPIView):
    serializer_class = RetrieveProductSer
    queryset = Product.objects.all()


class ProductSeriesView(ListAPIView):
    serializer_class = ProductSeriesSer
    queryset = Product.objects.all()

    def get_serializer_context(self):
        start_date = self.request.GET.get("start_date", None)
        end_date = self.request.GET.get("end_date", None)
        if start_date and end_date:
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        return {"start_date": start_date.date(), "end_date": end_date}


class ProductMonthView(ListAPIView):
    serializer_class = ProductMonthSer
    queryset = Product.objects.all()

    def get_serializer_context(self):
        year = self.request.GET.get("year", None)
        return {"year": year}


class ProductDepotMonthView(ListAPIView):
    serializer_class = ProductDepotMonthSer
    queryset = Product.objects.all()

    def get_serializer_context(self):
        year = self.request.GET.get("year", None)
        return {"year": year}


class ProductTopCustomerMonthView(ListAPIView):
    serializer_class = ProductTopCustomerMonthSer
    queryset = Product.objects.all().prefetch_related("sale_set")

    def get_serializer_context(self):
        year = self.request.GET.get("year", None)
        month = self.request.GET.get("month", None)

        return {"year": year, "month": month}
