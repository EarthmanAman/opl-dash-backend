from django.urls import path
from .views import (
    FrontendAppView,
)

app_name = "main"
urlpatterns = [
    path("", FrontendAppView.as_view(), name="frontend"),
    path("depots", FrontendAppView.as_view(), name="depots_redirect"),
    path("sale", FrontendAppView.as_view(), name="sales_redirect"),
    path("customers", FrontendAppView.as_view(), name="customers_redirect"),
]
