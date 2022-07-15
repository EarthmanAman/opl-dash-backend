import datetime
from django.db.models import F, FloatField, Sum, Count
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)

# Local imports
from product.models import Product
from .models import Depot


class RetrieveDepotSer(ModelSerializer):
    """Handle retrieve of depot

    Used:
        RetrieveSaleSer -> sale/serializers
    """

    class Meta:
        model = Depot
        fields = ["id", "name"]


class DepotMonthSer(ModelSerializer):
    revenue = SerializerMethodField()

    class Meta:
        model = Depot
        fields = [
            "id",
            "name",
            "revenue",
        ]

    def calc(self, obj, quantity, year):

        totals = (
            obj.sale_set.filter(date__year=year)
            .values("date__year", "date__month")
            .annotate(
                sum=Sum(F("selling_price") * F("vol_obs"), output_field=FloatField()),
                quantity=Sum("vol_obs"),
            )
        )

        return totals

    def get_revenue(self, obj):
        year = self.context.get("year", None)
        return self.calc(obj, False, year)


class DepotProductMonthSer(ModelSerializer):
    revenue = SerializerMethodField()

    class Meta:
        model = Depot
        fields = [
            "id",
            "name",
            "revenue",
        ]

    def calc(self, obj, year):
        products = Product.objects.all()
        sales = obj.sale_set.filter(date__year=year)
        prods = []
        for product in products:

            totals = (
                sales.filter(product=product)
                .values("date__year", "date__month")
                .annotate(
                    sum=Sum(
                        F("selling_price") * F("vol_obs"),
                        output_field=FloatField(),
                    ),
                    quantity=Sum("vol_obs"),
                )
            )
            prods.append({"name": product.name, "months": totals})

        return prods

    def get_revenue(self, obj):
        year = self.context["year"]
        return self.calc(obj, year)


class DepotSeriesSer(ModelSerializer):
    revenue = SerializerMethodField()

    class Meta:
        model = Depot
        fields = [
            "id",
            "name",
            "revenue",
        ]

    def calc(self, obj, start_date=None, end_date=None):

        if start_date and end_date:
            sales = (
                obj.sale_set.only("date", "selling_price", "vol_obs")
                .filter(date__gte=start_date)
                .filter(date__lte=end_date)
            ).order_by("-date")
        else:
            sales = obj.sale_set.all()
        totals = sales.values("date").annotate(
            sum=Sum(F("selling_price") * F("vol_obs"), output_field=FloatField()),
            quantity=Sum("vol_obs"),
        )
        return totals

    def get_revenue(self, obj):
        start_date = self.context["start_date"]
        end_date = self.context["end_date"]
        if start_date and end_date:
            return self.calc(obj, start_date, end_date)
        return self.calc(obj, False)


class DepotProductSeriesSer(ModelSerializer):
    revenue = SerializerMethodField()

    class Meta:
        model = Depot
        fields = [
            "id",
            "name",
            "revenue",
        ]

    def calc(self, obj, quantity, start_date, end_date):
        products = [
            product[0] for product in set(obj.sale_set.values_list("product__name"))
        ]
        prods = []
        for product in products:
            if start_date and end_date:
                sales = (
                    obj.sale_set.filter(product__name=product)
                    .filter(date__gte=start_date)
                    .filter(date__lte=end_date)
                )
            else:
                sales = obj.sale_set.filter(product__name=product)

            totals = sales.values("date").annotate(
                sum=Sum(F("selling_price") * F("vol_obs"), output_field=FloatField()),
                quantity=Sum("vol_obs"),
            )

            prods.append({"name": product, "data": totals})
        return prods

    def get_revenue(self, obj):
        start_date = self.context["start_date"]
        end_date = self.context["end_date"]
        if start_date and end_date:
            return self.calc(obj, False, start_date, end_date)
        return self.calc(obj, False)


class DepotCustomerMonthSer(ModelSerializer):
    revenue = SerializerMethodField()

    class Meta:
        model = Depot
        fields = [
            "id",
            "name",
            "revenue",
        ]

    def calc(self, obj, year, month):
        sales = obj.sale_set.filter(date__year=year)

        if month != 13:
            sales = (
                obj.sale_set.select_related("customer")
                .filter(date__year=year)
                .filter(date__month=month)
            )
        else:
            sales = obj.sale_set.select_related("customer").filter(date__year=year)

        totals = sales.values("customer__name").annotate(
            sum=Sum(F("selling_price") * F("vol_obs"), output_field=FloatField()),
            count=Count("id"),
            quantity=Sum("vol_obs"),
        )

        totals = totals.order_by("-sum")

        return totals

    def get_revenue(self, obj):
        year = self.context["year"]
        month = self.context["month"]
        return self.calc(obj, year, month)
