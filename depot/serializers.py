import datetime
from django.db.models import F, FloatField, Sum, Count
from rest_framework.serializers import (
	ModelSerializer, 
	SerializerMethodField,	
)

# Local imports
from product.models import Product
from . models import Depot

class RetrieveDepotSer(ModelSerializer):
    """Handle retrieve of depot

    Used:
        RetrieveSaleSer -> sale/serializers
    """
    class Meta:
        model = Depot
        fields = [
            "id",
            "name"
        ]

class DepotMonthSer(ModelSerializer):
    revenue = SerializerMethodField()
    quantity = SerializerMethodField()
    class Meta:
        model = Depot
        fields = [
            "id",
            "name",
            "revenue",
            "quantity",
        ]
    
    def calc(self, obj, quantity=False):
        years = [year[0] for year in set(obj.sale_set.values_list("date__year"))]
        y = []
        for year in years:
            if quantity:
                totals = obj.sale_set.filter(date__year=year).values("date__month").annotate(sum=Sum("vol_obs")).values("date__month", "sum")
            else:
                totals = obj.sale_set.filter(date__year=year).values("date__year", "date__month").annotate(sum=Sum(F("selling_price") * F('vol_obs'), output_field=FloatField()))\
                    .values("date__month", "sum").cache()
            # total = totals.aggregate(total=Sum("sum"))
            y.append({"year":year, "months":totals})
        return y

    def get_revenue(self, obj):
        return self.calc(obj)
    
    def get_quantity(self, obj):
        return self.calc(obj, True)

class DepotProductMonthSer(ModelSerializer):
    revenue = SerializerMethodField()
    quantity = SerializerMethodField()

    class Meta:
        model = Depot
        fields=[
            "id",
            "name",
            "revenue",
            "quantity",
        ]
    
    def calc(self, obj, quantity=False):
        years = [year[0] for year in set(obj.sale_set.values_list("date__year"))]
        products = Product.objects.all()
        y = []
        for year in years:
            sales = obj.sale_set.filter(date__year=year)
            prods = []
            for product in products:
                if quantity:
                    totals = sales.filter(product=product)\
                        .values("date__year", "date__month")\
                            .annotate(sum=Sum("vol_obs"))\
                                .values("date__month", "sum")
                else:
                    totals = sales.filter(product=product)\
                        .values("date__year", "date__month")\
                            .annotate(sum=Sum(F("selling_price") * F('vol_obs'), output_field=FloatField()))\
                                .values("date__month", "sum")
                prods.append({"name":product.name, "months":totals}) 

            y.append({"year":year, "products":prods})
        return y

    def get_revenue(self, obj):
        return self.calc(obj)
    
    def get_quantity(self, obj):
        return self.calc(obj, True)

class DepotSeriesSer(ModelSerializer):
    revenue = SerializerMethodField()
    quantity = SerializerMethodField()

    class Meta:
        model = Depot
        fields = [
            "id",
            "name",
            "revenue",
            "quantity",
        ]

    def calc(self, obj, quantity=False):
        
        sales = obj.sale_set.all()
        if quantity:
            totals = sales.values("date").annotate(sum=Sum("vol_obs"))
        else:
            totals = sales.values("date").annotate(sum=Sum(F("selling_price") * F('vol_obs'), output_field=FloatField()))
        t = []
        for total in totals:
            timestamp = int(datetime.datetime.combine(total["date"], datetime.datetime.min.time()).timestamp()) * 1000
            t.append({"date": total["date"], "timestamp": timestamp, "sum":  total["sum"]})
        return t
    
    def get_revenue(self, obj):
        return self.calc(obj)
    
    def get_quantity(self, obj):
        return self.calc(obj, True)


class DepotProductSeriesSer(ModelSerializer):
    revenue = SerializerMethodField()
    quantity = SerializerMethodField()

    class Meta:
        model = Depot
        fields = [
            "id",
            "name",
            "revenue",
            "quantity",
        ]

    def calc(self, obj, quantity=False):
        products = [product[0] for product in set(obj.sale_set.values_list("product__name"))]
        prods = []
        for product in products:
            sales = obj.sale_set.filter(product__name=product)
            if quantity:
                totals = sales.values("date").annotate(sum=Sum("vol_obs"))
            else:
                totals = sales.values("date").annotate(sum=Sum(F("selling_price") * F('vol_obs'), output_field=FloatField()))
            t = []
            for total in totals:
                timestamp = int(datetime.datetime.combine(total["date"], datetime.datetime.min.time()).timestamp()) * 1000
                t.append({"date": total["date"], "timestamp": timestamp, "sum":  total["sum"]})
            prods.append({"name":product, "data":t})
        return prods
    
    def get_revenue(self, obj):
        return self.calc(obj)
    
    def get_quantity(self, obj):
        return self.calc(obj, True)

class DepotCustomerMonthSer(ModelSerializer):
    revenue = SerializerMethodField()
    quantity = SerializerMethodField()
    class Meta:
        model = Depot
        fields = [
            "id",
            "name",
            "revenue",
            "quantity",
        ]
    
    def calc(self, obj, quantity=False):
        years = [year[0] for year in set(obj.sale_set.values_list("date__year"))]
        y = []
        for year in years:
            sales = obj.sale_set.filter(date__year=year)
            if quantity:
                annual_totals = sales.values("customer__name")\
                    .annotate(sum=Sum("vol_obs"), count=Count("id"))\
                    .values("customer__name", "sum", "count")

                totals = sales.values("customer__name", "date__month")\
                    .annotate(sum=Sum("vol_obs"), count=Count("id"))\
                    .values("customer__name", "date__month", "sum", "count")
            else:
                annual_totals = sales.values("customer__name")\
                    .annotate(sum=Sum(F("selling_price") * F('vol_obs'), output_field=FloatField()), count=Count("id"))\
                    .values("customer__name", "sum", "count")
                totals = sales.values("customer__name", "date__month")\
                    .annotate(sum=Sum(F("selling_price") * F('vol_obs'), output_field=FloatField()), count=Count("id"))\
                    .values("customer__name", "date__month", "sum", "count")
            totals = totals.order_by("-sum")
            annual_totals = annual_totals.order_by("-sum")
            months = []
            for month in range(1, 13):
                customer_month = totals.filter(date__month=month)
                months.append({"month":month, "customers":customer_month})
            y.append({"year":year, "months":months, "customers":annual_totals})
        return y

    def get_revenue(self, obj):
        return self.calc(obj)

    def get_quantity(self, obj):
        return self.calc(obj, True)


