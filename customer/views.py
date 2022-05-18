from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response

# Local imports
from . models import Customer, Driver, Truck

from . serializers import (
    # Create serializers
    CreateCustomerSer,
    RetrieveCustomerSer,

    # Drivers serializers
    CreateDriverSer,

    # Truck Serializers
    CreateTruckSer,
    TopCustomerMonthSer,
)


# Customer Views
class CreateCustomerView(ListCreateAPIView):
    serializer_class = CreateCustomerSer
    queryset = Customer.objects.all()

    def get(self, request, *args, **kwargs):
        entries = Customer.objects.all()
        serializer = RetrieveCustomerSer(entries, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CreateCustomerSer(data=request.data)

        if serializer.is_valid():
            sale = serializer.save()
            serializer = RetrieveCustomerSer(sale)
            return Response(serializer.data)
        else:
            print(serializer.errors)
# Driver Views
class CreateDriverView(ListCreateAPIView):
    serializer_class = CreateDriverSer
    queryset = Driver.objects.all()

# Driver Views
class CreateTruckView(ListCreateAPIView):
    serializer_class = CreateTruckSer
    queryset = Truck.objects.all()

class TopCustomerMonthView(RetrieveAPIView):
    serializer_class = TopCustomerMonthSer
    queryset = User.objects.all()


