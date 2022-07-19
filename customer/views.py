from django.contrib.auth.models import User
from django.core.cache import cache
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response

# Local imports
from .models import Customer, Driver, Truck
from depot.models import Depot, DepotCustomer
from .serializers import (
    # Create serializers
    CreateCustomerSer,
    RetrieveCustomerSer,
    # Drivers serializers
    CreateDriverSer,
    # Truck Serializers
    CreateTruckSer,
    RetrieveTruckSer,
    TopCustomerMonthSer,
    CustomerMonthSer,
)


# Customer Views
class CreateCustomerView(ListCreateAPIView):
    serializer_class = CreateCustomerSer
    queryset = Customer.objects.all()

    def get(self, request, *args, **kwargs):
        e = cache.get("customer", None)
        if e:
            return Response(e)
        else:
            entries = (
                Customer.objects.prefetch_related("truck_set").all().order_by("name")
            )
            serializer = RetrieveCustomerSer(entries, many=True)
            cache.set("customer", serializer.data)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CreateCustomerSer(data=request.data)

        if serializer.is_valid():
            customer = serializer.save()

            customers = (
                Customer.objects.all().order_by("name").prefetch_related("truck_set")
            )
            serializer = RetrieveCustomerSer(customers, many=True)
            cache.set("customer", serializer.data)
            return Response(serializer.data)
        else:
            None


class CreateC(ListCreateAPIView):
    serializer_class = CreateCustomerSer

    def get(self, request, *args, **kwargs):
        code = request.GET.get("code")
        name = request.GET.get("name")
        customer = Customer.objects.create(code=code, name=name)
        return Response({"status": "workd"})


class CustomerDetailView(RetrieveAPIView):
    serializer_class = CustomerMonthSer
    queryset = Customer.objects.all().prefetch_related("sale_set")

    def get(self, request, *args, **kwargs):
        # e = cache.get("customer-{}".format(self.kwargs["pk"]), None)
        # if e:
        #     return Response(e)
        # else:
        customer = Customer.objects.get(pk=int(self.kwargs["pk"]))
        serializer = CustomerMonthSer(customer)
        # cache.set("customer-{}".format(self.kwargs["pk"]), serializer.data)
        return Response(serializer.data)


# Driver Views
class CreateDriverView(ListCreateAPIView):
    serializer_class = CreateDriverSer
    queryset = Driver.objects.all()


# Add customer
class AddCustomer(ListCreateAPIView):
    serializer_class = CreateTruckSer

    def post(self, request, *args, **kwargs):

        customer = request.data.get("customer")
        depot = request.data.get("depot")

        if customer and depot:
            customer = Customer.objects.get(pk=int(customer))
            depot = Depot.objects.get(pk=int(depot))
            depots_customers = depot.depotcustomer_set.filter(customer=customer)
            if not depots_customers.exists():
                depot_customer = DepotCustomer.objects.create(
                    depot=depot, customer=customer
                )
            return Response({"status": "success"})
        else:
            return Response({"status": "fail"})


# Driver Views
class CreateTruckView(ListCreateAPIView):
    serializer_class = CreateTruckSer
    queryset = Truck.objects.all()

    def get(self, request, *args, **kwargs):
        e = cache.get("trucks", None)
        if not e:
            trucks = Truck.objects.filter(customer__name="ONE PET").prefetch_related(
                "driver"
            )
            serializer = RetrieveTruckSer(trucks, many=Truck)
            cache.set("trucks", serializer.data)
            return Response(serializer.data)
        return Response(e)

    def post(self, request, *args, **kwargs):

        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        customer_id = request.data.get("customer")
        plate_no = request.data.get("plate_no")
        if last_name:
            name = str(first_name) + " " + last_name
        else:
            name = first_name
        if first_name and last_name:

            if customer_id != None:
                customer = Customer.objects.get(pk=int(customer_id))
            else:
                customer = Customer.objects.get(name="ONE PET")
            trucks = Truck.objects.filter(plate_no=plate_no)
            if trucks.exists():
                truck = trucks.last()
                driver = truck.driver
                driver.name = name
                driver.save()

                truck.driver = driver
                truck.customer = customer
                truck.plate_no = plate_no
                truck.save()
            else:
                driver = Driver.objects.create(name=name)
                truck = Truck.objects.create(
                    customer=customer, plate_no=plate_no, driver=driver
                )

            serializer = RetrieveTruckSer(truck)
            return Response(serializer.data)
        else:
            Response(
                {
                    "status": "failed",
                    "message": "Something went wrong check your inputs or contact admin",
                }
            )


class TopCustomerMonthView(RetrieveAPIView):
    serializer_class = TopCustomerMonthSer
    queryset = User.objects.all()

    def get_serializer_context(self):
        year = self.request.GET.get("year", None)
        month = self.request.GET.get("month", None)

        return {"year": year, "month": month}

    def get(self, request, *args, **kwargs):
        context = self.get_serializer_context()
        # e = cache.get(
        #     "top-customer-{}-{}".format(context["year"], context["month"]), None
        # )
        # if e:
        #     # cache.delete("top-customer")
        #     return Response(e)
        # else:
        user = User.objects.get(pk=int(self.kwargs["pk"]))

        serializer = TopCustomerMonthSer(user, context=context)
        # cache.set(
        #     "top-customer-{}-{}".format(context["year"], context["month"]),
        #     serializer.data,
        # )
        return Response(serializer.data)
