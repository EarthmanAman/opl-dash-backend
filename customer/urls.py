from django.urls import path
from . views import (
    # Customer Views
    CreateCustomerView,

    # Driver Views
    CreateDriverView,

    # Truck Views
    CreateTruckView,
)

app_name = "customer"

urlpatterns = [
     # Customer urls
     path('', CreateCustomerView.as_view(), name="customer"),

     # Driver urls
     path('drivers/', CreateDriverView.as_view(), name="drivers"),

     # Truck urls
     path('trucks/', CreateTruckView.as_view(), name="trucks"),
]
