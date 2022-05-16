from rest_framework.serializers import (
	ModelSerializer, 
	SerializerMethodField,	
	)
from . models import Customer, Driver, Truck

# Customer Serializers
class CreateCustomerSer(ModelSerializer):

    class Meta:
        model = Customer
        fields = [
            "code",
            "name",
        ]

class RetrieveCustomerSer(ModelSerializer):
    """Handle retrieve and update requests

    Used in:
        RetrieveSaleSer -> sales.serializers
    """
    class Meta:
        model = Customer
        fields = [
            "id",
            "code",
            "name",
        ]

# Drivers Serializers
class CreateDriverSer(ModelSerializer):

    class Meta:
        model = Driver
        fields = [
            "first_name",
            "last_name",
        ]

class RetrieveDriverSer(ModelSerializer):
    """Handle retrieve of driver

    Used:
        RetrieveTruckSer -> customer.serializers
    """
    class Meta:
        model = Driver
        fields = [
            "id",
            "first_name",
            "last_name",
        ]

# Truck Serializers
class CreateTruckSer(ModelSerializer):

    class Meta:
        model = Truck
        fields = [
            "driver",
            "plate_no",
            "is_hired",
        ]

class RetrieveTruckSer(ModelSerializer):
    """Handle retrieve and update requests

    Used in:
        RetrieveSaleSer -> sales.serializers
    """
    driver = SerializerMethodField()

    class Meta:
        model = Truck
        fields = [
            "id"
            "driver",
            "plate_no",
            "is_hired",
        ]
    
    def get_driver(self, obj):
        return RetrieveDriverSer(obj.driver).data