from rest_framework.serializers import (
	ModelSerializer, 
	SerializerMethodField,	
)

# Local imports
from . models import Depot

class RetrieveDepotSer(ModelSerializer):
    """Handle retrieve of depot

    Used:
        RetrieveSaleSer -> sale/serializers
    """
    class Meta:
        model = Depot
        fields = [
            "name"
        ]