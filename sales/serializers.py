from ast import Str
from dataclasses import fields
from itertools import product
from typing import Dict
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)

from customer.serializers import RetrieveCustomerSer, RetrieveTruckSer
from depot.serializers import RetrieveDepotSer
from product.serializers import RetrieveProductSer

from .models import Sale


class CreateSaleSer(ModelSerializer):
    class Meta:
        model = Sale
        fields = [
            "customer",
            "depot",
            "product",
            "truck",
            "entry_no",
            "date",
            "is_paid",
            "is_loaded",
            "lpo_no",
            "order_no",
            "selling_price",
            "vol_obs",
            "vol_20",
            "amount_paid",
            "seal_no",
            "remarks",
            "loading_date",
        ]


class RetrieveSaleSer(ModelSerializer):
    customer = SerializerMethodField()
    depot = SerializerMethodField()
    product = SerializerMethodField()
    truck = SerializerMethodField()

    class Meta:
        model = Sale
        fields = [
            "customer",
            "depot",
            "product",
            "truck",
            "entry_no",
            "date",
            "is_paid",
            "is_loaded",
            "lpo_no",
            "order_no",
            "selling_price",
            "vol_obs",
            "vol_20",
        ]

    def get_customer(self, obj) -> Str:
        return obj.customer.name

    def get_depot(self, obj) -> Str:
        return obj.depot.name

    def get_product(self, obj) -> Str:
        return obj.product.name

    def get_truck(self, obj) -> Str:
        if obj.truck == None:
            return {"plate_no": None, "driver": None}
        return {"plate_no": obj.truck.plate_no, "driver": obj.truck.driver.first_name}
