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

    def calc(self, obj, quantity=False, start_date=None, end_date=None):
        if quantity:
            if start_date and end_date:
                totals = (
                    obj.sale_set.filter(date__gte=start_date)
                    .filter(date__lte=end_date)
                    .values("date")
                    .annotate(sum=Sum("vol_obs"))
                )
            else:
                totals = obj.sale_set.values("date").annotate(sum=Sum("vol_obs"))
        else:
            if start_date and end_date:
                totals = (
                    obj.sale_set.filter(date__gte=start_date)
                    .filter(date__lte=end_date)
                    .values("date")
                    .annotate(
                        sum=Sum(
                            F("selling_price") * F("vol_obs"), output_field=FloatField()
                        )
                    )
                )
            else:
                totals = obj.sale_set.values("date").annotate(
                    sum=Sum(
                        F("selling_price") * F("vol_obs"), output_field=FloatField()
                    )
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
        start_date = self.context["start_date"]
        end_date = self.context["end_date"]
        if start_date and end_date:

            return self.calc(obj, False, start_date, end_date)
        return self.calc(obj, False)

    def get_quantity(self, obj):
        start_date = self.context["start_date"]
        end_date = self.context["end_date"]
        if start_date and end_date:
            return self.calc(obj, True, start_date, end_date)

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

    def calc(self, obj, quantity, year):

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

        return totals.order_by("date__month")

    def get_revenue(self, obj):
        year = self.context.get("year", None)
        return self.calc(obj, False, year)

    def get_quantity(self, obj):
        year = self.context.get("year", None)
        return self.calc(obj, True, year)


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

    def calc(self, obj, quantity, year, month):

        sales = obj.sale_set.filter(date__year=year)
        if quantity:
            if month != "False":
                totals = (
                    sales.values("customer__name", "date__month")
                    .annotate(sum=Sum("vol_obs"))
                    .values("customer__name", "date__month", "sum")
                )
            else:
                totals = (
                    sales.values("customer__name")
                    .annotate(sum=Sum("vol_obs"))
                    .values("customer__name", "sum")
                )

        else:
            if month != "False":
                totals = (
                    sales.values("customer__name", "date__month")
                    .annotate(
                        sum=Sum(
                            F("selling_price") * F("vol_obs"), output_field=FloatField()
                        )
                    )
                    .values("customer__name", "date__month", "sum")
                )
            else:
                totals = (
                    sales.values("customer__name")
                    .annotate(
                        sum=Sum(
                            F("selling_price") * F("vol_obs"), output_field=FloatField()
                        )
                    )
                    .values("customer__name", "sum")
                )
        totals = totals.order_by("-sum")
        if month != "False":
            months = []
            for month in range(1, 13):
                customer_month = totals.filter(date__month=month)[:10]
                months.append({"month": month, "customers": customer_month})

            return months
        return totals

    def get_revenue(self, obj):
        year = self.context["year"]
        month = self.context["month"]
        return self.calc(obj, False, year, month)

    def get_quantity(self, obj):
        year = self.context["year"]
        month = self.context["month"]
        return self.calc(obj, True, year, month)
