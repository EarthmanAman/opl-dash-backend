from rest_framework.generics import ListCreateAPIView

# Local imports
from . models import Customer, Driver, Truck

from . serializers import (
    # Create serializers
    CreateCustomerSer,

    # Drivers serializers
    CreateDriverSer,

    # Truck Serializers
    CreateTruckSer,
)


# Customer Views
class CreateCustomerView(ListCreateAPIView):
    serializer_class = CreateCustomerSer
    queryset = Customer.objects.all()

# Driver Views
class CreateDriverView(ListCreateAPIView):
    serializer_class = CreateDriverSer
    queryset = Driver.objects.all()

# Driver Views
class CreateTruckView(ListCreateAPIView):
    serializer_class = CreateTruckSer
    queryset = Truck.objects.all()