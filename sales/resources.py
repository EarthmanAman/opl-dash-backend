from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

from customer.models import Customer, Truck
from depot.models import Depot
from product.models import Product

from . models import Sale

class SaleResource(resources.ModelResource):
    # customer = fields.Field(
    #     column_name='customer',
    #     attribute ='customer',
    #     widget=ForeignKeyWidget(Customer, 'name'))
    # depot = fields.Field(
    #     widget=ForeignKeyWidget(Depot, 'name'))
    # product = fields.Field(
    #     widget=ForeignKeyWidget(Product, 'name'))
    # truck = fields.Field(
    #     widget=ForeignKeyWidget(Truck, 'plate_no'))

    class Meta:
        model = Sale
        fields = (
            "id",
            "customer__name", 
            "depot__name", 
            "product__name", 
            "truck__plate_no", 
            "entry_no", 
            "date", 
            "is_paid", 
            "is_loaded", 
            "lpo_no", 
            "order_no", 
            "selling_price",
            "vol_obs",
            "vol_20",
        )

