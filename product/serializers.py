import datetime
from django.db.models import F, FloatField, Sum
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)

# Local imports
from .models import Product


class RetrieveProductSer(ModelSerializer):
    """Handle retrieve of product

    Used:
        RetrieveSaleSer -> sales.serializers
    """

    class Meta:
        model = Product
        fields = ["id", "name"]


class ProductSeriesSer(ModelSerializer):
    revenue = SerializerMethodField()
    # quantity = SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "name",
            "revenue",
            # "quantity",
        ]

    def calc(self, obj, quantity=False, start_date=None, end_date=None):

        totals = (
            obj.sale_set.only("date", "selling_price", "vol_obs")
            .filter(date__gte=start_date, date__lte=end_date)
            .values("date")
            .annotate(
                sum=Sum(F("selling_price") * F("vol_obs"), output_field=FloatField()),
                quantity=Sum("vol_obs"),
            )
            .order_by("-date")
        )

        return totals

    def get_revenue(self, obj):
        start_date = self.context["start_date"]
        end_date = self.context["end_date"]
        return self.calc(obj, False, start_date, end_date)


class ProductMonthSer(ModelSerializer):
    revenue = SerializerMethodField()
    # quantity = SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "name",
            "revenue",
            # "quantity",
        ]

    def calc(self, obj, quantity, year):
        totals = (
            obj.sale_set.only("date", "selling_price", "vol_obs")
            .filter(date__year=year)
            .values("date__year", "date__month")
            .annotate(
                sum=Sum(F("selling_price") * F("vol_obs"), output_field=FloatField()),
                quantity=Sum("vol_obs"),
            )
        )

        return totals.order_by("date__month")

    def get_revenue(self, obj):
        year = self.context.get("year", None)
        return self.calc(obj, False, year)


class ProductDepotMonthSer(ModelSerializer):
    revenue = SerializerMethodField()
    # quantity = SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "name",
            "revenue",
            # "quantity",
        ]

    def calc(self, obj, year):
        totals = (
            obj.sale_set.values("date__year", "date__month", "depot__name")
            .filter(date__year=year)
            .annotate(
                sum=Sum(F("selling_price") * F("vol_obs"), output_field=FloatField()),
                quantity=Sum("vol_obs"),
            )
        )

        return totals

    def get_revenue(self, obj):
        year = self.context["year"]
        return self.calc(obj, year)


class ProductTopCustomerMonthSer(ModelSerializer):
    revenue = SerializerMethodField()
    # quantity = SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "revenue",
            # "quantity",
        ]

    def calc(self, obj, year, month):

        sales = obj.sale_set.filter(date__year=year)

        if month != "False":
            totals = sales.values("customer__name", "date__month").annotate(
                sum=Sum(F("selling_price") * F("vol_obs"), output_field=FloatField()),
                quntity=Sum("vol_obs"),
            )
        else:
            totals = sales.values("customer__name").annotate(
                sum=Sum(F("selling_price") * F("vol_obs"), output_field=FloatField()),
                quantity=Sum("vol_obs"),
            )
        totals = totals.order_by("customer__name", "date__month", "-sum")
        # if month != "False":
        #     months = []
        #     for month in range(1, 13):
        #         customer_month = totals.filter(date__month=month)[:10]
        #         months.append({"month": month, "customers": customer_month})

        #     return months
        return totals

    def get_revenue(self, obj):
        year = self.context["year"]
        month = self.context["month"]
        return self.calc(obj, year, month)

    # def get_quantity(self, obj):
    #     year = self.context["year"]
    #     month = self.context["month"]
    #     return self.calc(obj, True, year, month)
