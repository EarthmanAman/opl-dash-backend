import datetime
import csv
import openpyxl
import xlrd
import codecs
import threading
from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from customer.models import Customer, Driver, Truck
from depot.models import Depot
from product.models import Product

from sales.resources import SaleResource

# Local imports
from .models import Sale
from .serializers import CreateSaleSer, RetrieveSaleSer

from tablib import Dataset


def simple_upload(request):
    if request.method == "POST":
        person_resource = SaleResource()
        dataset = Dataset()
        new_persons = request.FILES["myfile"]

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(
            dataset, dry_run=True
        )  # Test the data import
        print(result.has_errors())
        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, "simple_upload.html")


class CreateSaleView(ListCreateAPIView):
    serializer_class = CreateSaleSer
    queryset = Sale.objects.all().select_related()

    def get(self, request, *args, **kwargs):
        start_date = request.GET.get("start_date", None)
        end_date = request.GET.get("end_date", None)
        depot = request.GET.get("depot", None)
        if start_date != None and end_date != None:
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
            if depot != "staff":

                entries = (
                    Sale.objects.select_related("depot", "customer", "truck", "product")
                    .filter(depot__name=depot)
                    .filter(date__gte=start_date)
                    .filter(date__lte=end_date)
                    .order_by("-date")
                )

            else:
                entries = (
                    Sale.objects.select_related("depot", "customer", "truck", "product")
                    .filter(date__gte=start_date)
                    .filter(date__lte=end_date)
                    .order_by("-date")
                )
        else:
            entries = Sale.objects.select_related(
                "depot", "customer", "truck", "product"
            ).all()
        serializer = RetrieveSaleSer(entries, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CreateSaleSer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            sale = serializer.save()
            start_date = request.GET.get("start_date", None)
            end_date = request.GET.get("end_date", None)

            if start_date != None and end_date != None:
                start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
                end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
                entries = (
                    Sale.objects.filter(date__gte=start_date)
                    .filter(date__lte=end_date)
                    .order_by("-date")
                    .select_related()
                )
            else:
                entries = Sale.objects.all().select_related()

            serializer = RetrieveSaleSer(entries, many=True)
            return Response(serializer.data)
        else:
            print(serializer.errors)


class RetrieveSaleView(RetrieveUpdateAPIView):
    serializer_class = RetrieveSaleSer
    queryset = Sale.objects.all()


# class UploadExcel(APIView):
#     parser_classes = (MultiPartParser,)

#     def post(self, request, *args, **kwargs):
#         sale_resource = SaleResource()
#         dataset = Dataset()
#         file = request.FILES["file"]
#         r = file.read()
#         imported_data = dataset.load(r)
#         result = sale_resource.import_data(
#             dataset, dry_run=True
#         )  # Test the data import
#         if not result.has_errors():
#             # sale_resource.import_data(dataset, dry_run=False)  # Actually import now
#             return Response(
#                 {"status": status.HTTP_201_CREATED, "message": "Upload successful"}
#             )
#         return Response(
#             {
#                 "status": status.HTTP_403_FORBIDDEN,
#                 "message": "Check your file format. If error persist contact admin",
#             }
#         )


def check_headers(file):
    check = False
    if file.name.endswith(".csv"):
        reader = csv.reader(codecs.iterdecode(file, "utf-8"))
        headers = next(reader)
    elif file.name.endswith(".xlsx"):

        wb = openpyxl.load_workbook(file)
        ws = wb.active
        reader = list(ws.iter_rows(values_only=True))
        headers = reader[1]
        reader = reader[2:]
    elif file.name.endswith(".xls"):
        workbook = xlrd.open_workbook(file_contents=file.read())
        sheet = workbook.sheet_by_index(0)
        data = [sheet.row_values(rowx) for rowx in range(sheet.nrows)]
        headers = data[1]
        reader = data[2:]

    my_headers = [
        "DATE",
        "PRODUCT",
        "CUSTOMER",
        "TRUCK",
        "DRIVER",
        "ORDER NO",
        "LPO_NO",
        "ENTRY NO",
        "SEAL NO",
        "VOL OBS",
        "VOL 20",
        "SELLING PRICE",
        "PAYMENT",
        "AMOUNT PAID",
        "LOADING DATE",
        "REMARKS",
    ]
    if list(headers) == my_headers:
        check = True

    return check, reader


def upload(row, depot, save):
    date = row[0]
    product = row[1]
    customer = row[2]
    truck = row[3]
    driver = row[4]
    order_no = row[5]
    lpo_no = row[6]
    entry_no = row[7]
    seal_no = row[8]
    vol_obs = int(row[9])
    vol_20 = int(row[10]) if row[10] != None else row[10]
    selling_price = float(row[11])
    is_paid = True if row[12] == "Yes" else False
    amount_paid = int(row[13]) if row[13] != None else None
    loading_date = row[14]
    remarks = row[15]
    customer = Customer.objects.get(name=customer)

    product = Product.objects.get(name=product)

    if save:
        trucks = Truck.objects.filter(plate_no=truck)
        if trucks.exists():
            truck = trucks.last()
            if truck.driver.name != driver:
                driver = Driver.objects.create(name=driver)
                truck.driver = driver
                truck.save()
        else:
            if truck:
                driver = Driver.objects.create(name=driver)
                truck = Truck.objects.create(
                    customer=None, plate_no=truck, driver=driver
                )
        sales = Sale.objects.filter(order_no=order_no)
        exist = False
        print(sales)
        for sale in sales:
            if (
                sale.entry_no == entry_no
                and sale.vol_obs == float(vol_obs)
                and sale.vol_20 == float(vol_20)
                and sale.product == product
                and sale.customer == customer
            ):
                exist = True
        if not exist:
            sale = Sale.objects.create(
                product=product,
                depot=depot,
                truck=truck,
                customer=customer,
                date=date,
                order_no=order_no,
                lpo_no=lpo_no,
                entry_no=entry_no,
                vol_obs=vol_obs,
                vol_20=vol_20,
                selling_price=selling_price,
                is_paid=is_paid,
                seal_no=seal_no,
                amount_paid=amount_paid,
                loading_date=loading_date,
                remarks=remarks,
            )
    else:
        trucks = Truck.objects.filter(plate_no=truck)
        if trucks.exists():
            truck = trucks.last()
            if truck.driver.name != driver:
                driver = Driver(name=driver)
                truck.driver = driver
        else:
            driver = Driver(name=driver)
            truck = Truck(plate_no=truck, driver=driver)
        sale = Sale(
            product=product,
            depot=depot,
            truck=truck,
            date=date,
            order_no=order_no,
            lpo_no=lpo_no,
            entry_no=entry_no,
            vol_obs=vol_obs,
            vol_20=vol_20,
            selling_price=selling_price,
            is_paid=is_paid,
            seal_no=seal_no,
            amount_paid=amount_paid,
            loading_date=loading_date,
            remarks=remarks,
        )
    return True


def up(reader, depot, save):
    for row in reader:
        succesful = upload(row, depot, save=save)
        if not succesful:
            return False
    return True


class HandleExcelUpload(threading.Thread):
    def __init__(self, reader, depot):
        self.reader = reader
        self.depot = depot

        threading.Thread.__init__(self)

    def run(self):
        print("*" * 100)
        up(self.reader, self.depot, True)


class UploadExcel(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        file = request.FILES["file"]
        check, reader = check_headers(file)
        depot = Depot.objects.filter(pk=int(self.kwargs.get("depot_id")))
        if not depot.exists():
            return Response(
                {"status": "fail", "message": "An error occured contact admin."}
            )
        elif check:
            depot = depot.last()

            succesful = up(reader, depot, save=False)
            if succesful == False:
                return Response(
                    {
                        "status": "fail",
                        "message": "Error in the data. Please check or contact admin.",
                    }
                )
            HandleExcelUpload(reader, depot).start()

            return Response({"status": "success", "message": "Uploaded successful"})
        else:

            return Response(
                {"status": "fail", "message": "Make sure the file used is correct."}
            )
