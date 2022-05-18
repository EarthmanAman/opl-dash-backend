
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls", namespace="accounts")),
    path('customer/', include("customer.urls", namespace="customer")),
    path('depot/', include("depot.urls", namespace="depot")),
    path('product/', include("product.urls", namespace="product")),
    path('sales/', include("sales.urls", namespace="sales")),
    path('silk/', include('silk.urls', namespace='silk')),
]
