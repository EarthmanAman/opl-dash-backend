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
    quantity = SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "name",
            "revenue",
            "quantity",
        ]

    def calc(self, obj, quantity=False):
        if quantity:
            totals = obj.sale_set.values("date").annotate(sum=Sum("vol_obs"))
        else:
            totals = obj.sale_set.values("date").annotate(
                sum=Sum(F("selling_price") * F("vol_obs"), output_field=FloatField())
            )
        t = []
        for total in totals.order_by("-date"):
            timestamp = (
                int(
                    datetime.datetime.combine(
                        total["date"], datetime.datetime.min.time()
                    ).timestamp()
                )
                * 1000
            )
            t.append(
                {
                    "date": total["date"],
                    "timestamp": timestamp,
                    "sum": total["sum"],
                }
            )
        return t

    def get_revenue(self, obj):
        return self.calc(obj)

    def get_quantity(self, obj):
        return self.calc(obj, True)


class ProductMonthSer(ModelSerializer):
    revenue = SerializerMethodField()
    quantity = SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "name",
            "revenue",
            "quantity",
        ]

    def calc(self, obj, quantity=False):
        years = [year[0] for year in set(obj.sale_set.values_list("date__year"))]
        y = []
        for year in years:
            if quantity:
                totals = (
                    obj.sale_set.filter(date__year=year)
                    .values("date__month")
                    .annotate(sum=Sum("vol_obs"))
                    .values("date__month", "sum")
                )
            else:
                totals = (
                    obj.sale_set.filter(date__year=year)
                    .values("date__year", "date__month")
                    .annotate(
                        sum=Sum(
                            F("selling_price") * F("vol_obs"), output_field=FloatField()
                        )
                    )
                    .values("date__month", "sum")
                )

            y.append({"year": year, "months": totals.order_by("date__month")})
        return y

    def get_revenue(self, obj):
        return self.calc(obj)

    def get_quantity(self, obj):
        return self.calc(obj, True)


class ProductDepotMonthSer(ModelSerializer):
    revenue = SerializerMethodField()
    quantity = SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "name",
            "revenue",
            "quantity",
        ]

    def calc(self, obj, quantity=False):
        years = [year[0] for year in set(obj.sale_set.values_list("date__year"))]
        # depots = [depot[0] for depot in set(obj.sale_set.values_list("depot__name"))]
        y = []
        for year in years:
            sales = obj.sale_set.filter(date__year=year)
            if quantity:
                totals = (
                    sales.values("date__month", "depot__name")
                    .annotate(sum=Sum("vol_obs"))
                    .values("date__month", "depot__name", "sum")
                )
            else:
                totals = (
                    sales.values("date__month", "depot__name")
                    .annotate(
                        sum=Sum(
                            F("selling_price") * F("vol_obs"), output_field=FloatField()
                        )
                    )
                    .values("date__month", "depot__name", "sum")
                )

            y.append(
                {
                    "year": year,
                    "months": totals.order_by("date__month").order_by("depot__name"),
                }
            )
        return y

    def get_revenue(self, obj):
        return self.calc(obj)

    def get_quantity(self, obj):
        return self.calc(obj, True)


class ProductTopCustomerMonthSer(ModelSerializer):
    revenue = SerializerMethodField()
    quantity = SerializerMethodField()

    class Meta:
        model = Product
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
                annual_totals = (
                    sales.values("customer__name")
                    .annotate(sum=Sum("vol_obs"))
                    .values("customer__name", "sum")
                )

                totals = (
                    sales.values("customer__name", "date__month")
                    .annotate(sum=Sum("vol_obs"))
                    .values("customer__name", "date__month", "sum")
                )
            else:
                annual_totals = (
                    sales.values("customer__name")
                    .annotate(
                        sum=Sum(
                            F("selling_price") * F("vol_obs"), output_field=FloatField()
                        )
                    )
                    .values("customer__name", "sum")
                )
                totals = (
                    sales.values("customer__name", "date__month")
                    .annotate(
                        sum=Sum(
                            F("selling_price") * F("vol_obs"), output_field=FloatField()
                        )
                    )
                    .values("customer__name", "date__month", "sum")
                )
            totals = totals.order_by("-sum")
            annual_totals = annual_totals.order_by("-sum")[:10]
            months = []
            for month in range(1, 13):
                customer_month = totals.filter(date__month=month)[:10]
                months.append({"month": month, "customers": customer_month})
            y.append({"year": year, "months": months, "customers": annual_totals})
        return y

    def get_revenue(self, obj):
        return self.calc(obj)

    def get_quantity(self, obj):
        return self.calc(obj, True)
