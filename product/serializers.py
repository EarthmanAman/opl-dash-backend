from rest_framework.serializers import (
    ModelSerializer,
)

# Local imports
from . models import Product

class RetrieveProductSer(ModelSerializer):
    """Handle retrieve of product

    Used:
        RetrieveSaleSer -> sales.serializers
    """
    class Meta:
        model = Product
        fields = [
            "id",
            "name"
        ]