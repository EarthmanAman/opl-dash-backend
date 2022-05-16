from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
)

# Local imports
from . models import Sale
from . serializers import (
    CreateSaleSer,
    RetrieveSaleSer
)

class CreateSaleView(ListCreateAPIView):
    serializer_class = CreateSaleSer
    queryset = Sale.objects.all()

class RetrieveSaleView(RetrieveUpdateAPIView):
    serializer_class = RetrieveSaleSer
    queryset = Sale.objects.all()