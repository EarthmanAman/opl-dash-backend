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

class DepotProductMonthView(ListAPIView):
    serializer_class = DepotProductMonthSer
    queryset = Depot.objects.all().prefetch_related("sale_set")

class DepotSeriesView(ListAPIView):
    serializer_class = DepotSeriesSer
    queryset = Depot.objects.all().prefetch_related("sale_set")

class DepotProductSeriesView(ListAPIView):
    serializer_class = DepotProductSeriesSer
    queryset = Depot.objects.all().prefetch_related("sale_set")

class DepotCustomerMonthView(ListAPIView):
    serializer_class = DepotCustomerMonthSer
    queryset = Depot.objects.all().prefetch_related("sale_set")


