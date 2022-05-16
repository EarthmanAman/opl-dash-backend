from django.urls import path
from . views import (
    CreateSaleView,
    RetrieveSaleView,
)

app_name = "sales"

urlpatterns = [
     path('', CreateSaleView.as_view(), name="sales"),
     path('<int:pk>/', RetrieveSaleView.as_view(), name="sales_retrieve")
]
