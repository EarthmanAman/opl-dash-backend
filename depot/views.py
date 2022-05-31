from calendar import month
import datetime
from rest_framework.generics import ListAPIView, RetrieveAPIView
from depot.models import Depot

from depot.serializers import (
    RetrieveDepotSer,
    DepotMonthSer,
    DepotProductMonthSer,
    DepotSeriesSer,
    DepotProductSeriesSer,
    DepotCustomerMonthSer,
)


class DepotListView(ListAPIView):
    serializer_class = RetrieveDepotSer
    queryset = Depot.objects.all()


class DepotMonthView(ListAPIView):
    serializer_class = DepotMonthSer
    queryset = Depot.objects.all().prefetch_related("sale_set")

    def get_serializer_context(self):
        year = self.request.GET.get("year", None)
        return {"year": year}


class DepotProductMonthView(ListAPIView):
    serializer_class = DepotProductMonthSer
    queryset = Depot.objects.all().prefetch_related("sale_set")

    def get_serializer_context(self):
        year = self.request.GET.get("year", None)
        return {"year": year}


class DepotSeriesView(RetrieveAPIView):
    serializer_class = DepotSeriesSer
    queryset = Depot.objects.all().prefetch_related("sale_set")

    def get_serializer_context(self):
        start_date = self.request.GET.get("start_date", None)
        end_date = self.request.GET.get("end_date", None)
        if start_date and end_date:
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        return {"start_date": start_date, "end_date": end_date}


class DepotProductSeriesView(RetrieveAPIView):
    serializer_class = DepotProductSeriesSer
    queryset = Depot.objects.all().prefetch_related("sale_set")

    def get_serializer_context(self):
        start_date = self.request.GET.get("start_date", None)
        end_date = self.request.GET.get("end_date", None)
        if start_date and end_date:
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        return {"start_date": start_date, "end_date": end_date}


class DepotCustomerMonthView(RetrieveAPIView):
    serializer_class = DepotCustomerMonthSer
    queryset = Depot.objects.all().prefetch_related("sale_set")

    def get_serializer_context(self):
        year = self.request.GET.get("year", None)
        month = int(self.request.GET.get("month", None))
        return {"year": year, "month": month}
