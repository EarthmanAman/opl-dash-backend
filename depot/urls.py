from django.urls import path
from . views import (
    DepotListView,
    DepotMonthView,
    DepotProductMonthView,
    DepotSeriesView,
    DepotProductSeriesView,
    DepotCustomerMonthView
)

app_name = "depot"

urlpatterns = [
     path('', DepotListView.as_view(), name="depot"),
     path('month/', DepotMonthView.as_view(), name="month"),
     path('product/month/', DepotProductMonthView.as_view(), name="product_month"),
     path('series/', DepotSeriesView.as_view(), name="depot_series"),
     path('product/series/', DepotProductSeriesView.as_view(), name="product_series"),
     path('customer/', DepotCustomerMonthView.as_view(), name="depot_customer"),
]
