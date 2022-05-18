from django.contrib.auth.models import User
from django.db.models import F, FloatField, Sum
from rest_framework.serializers import (
	ModelSerializer, 
	SerializerMethodField,	
	)
from . models import Customer, Driver, Truck
from sales.models import Sale

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

class TopCustomerMonthSer(ModelSerializer):
    revenue = SerializerMethodField()
    quantity = SerializerMethodField()
    class Meta:
        model = User
        fields = [
            "revenue",
            "quantity",
        ]
    
    def calc(self, quantity=False):
        years = [year[0] for year in set(Sale.objects.values_list("date__year"))]
        y = []
        for year in years:
            sales = Sale.objects.filter(date__year=year)
            if quantity:
                annual_totals = sales.values("customer__name")\
                    .annotate(sum=Sum("vol_obs"))\
                    .values("customer__name", "sum")

                totals = sales.values("customer__name", "date__month")\
                    .annotate(sum=Sum("vol_obs"))\
                    .values("customer__name", "date__month", "sum")
            else:
                annual_totals = sales.values("customer__name")\
                    .annotate(sum=Sum(F("selling_price") * F('vol_obs'), output_field=FloatField()))\
                    .values("customer__name", "sum")
                totals = sales.values("customer__name", "date__month")\
                    .annotate(sum=Sum(F("selling_price") * F('vol_obs'), output_field=FloatField()))\
                    .values("customer__name", "date__month", "sum")
            totals = totals.order_by("-sum")
            annual_totals = annual_totals.order_by("-sum")
            months = []
            for month in range(1, 13):
                customer_month = totals.filter(date__month=month)
                months.append({"month":month, "customers":customer_month})
            y.append({"year":year, "months":months, "customers":annual_totals})
        return y

    def get_revenue(self, obj):
        return self.calc()

    def get_quantity(self, obj):
        return self.calc(True)
