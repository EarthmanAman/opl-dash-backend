from django.urls import path
from . views import (
    # Customer Views
    CreateCustomerView,
    TopCustomerMonthView,

    # Driver Views
    CreateDriverView,

    # Truck Views
    CreateTruckView,
)

app_name = "customer"

urlpatterns = [
     # Customer urls
     path('', CreateCustomerView.as_view(), name="customer"),
     path('top/month/<int:pk>/', TopCustomerMonthView.as_view(), name="top_customer_month"),

     # Driver urls
     path('drivers/', CreateDriverView.as_view(), name="drivers"),

     # Truck urls
     path('trucks/', CreateTruckView.as_view(), name="trucks"),
]
