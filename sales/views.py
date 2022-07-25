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
        sales = Sale.objects.values("order_no").filter(
            order_no=request.data["order_no"]
        )
        if sales.exists():
            return Response(
                {
                    "status": "fail",
                    "message": "Another sale with the given order_no already exist in the system. Please check the order no.",
                }
            )
        serializer = CreateSaleSer(data=request.data)
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
            None


class RetrieveSaleView(RetrieveUpdateAPIView):
    serializer_class = RetrieveSaleSer
    queryset = Sale.objects.all()


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
    print(headers)
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
        "LOADING DATE",
        "REMARKS",
    ]
    if my_headers == list(headers)[:-1]:
        check = True

    return check, reader


def float_conversion_check(value, name):
    try:
        value = float(value)
        return value
    except:
        return f"One of the sales has {name} which is not a number"


def upload(row, depot, save):
    try:
        date = row[0]
        product = row[1]
        customer = row[2]
        truck = row[3]
        driver = row[4]
        order_no = row[5]
        lpo_no = row[6]
        entry_no = row[7]
        seal_no = row[8]
        vol_obs = (
            float_conversion_check(row[9], "Vol OBS") if row[9] != None else row[9]
        )
        vol_20 = (
            float_conversion_check(row[10], "Vol @ 20") if row[10] != None else row[10]
        )

        selling_price = (
            float_conversion_check(row[11], "Selling Price")
            if row[11] != None
            else row[11]
        )
        is_paid = True if row[12] == "Yes" else False
        # amount_paid = int(row[13]) if row[13] != None else None
        loading_date = row[14]
        remarks = row[15]

        if order_no == None:
            return [
                False,
                "One of the sales does not have an order no. Please check before uploading again.",
            ]
        elif vol_obs == None:
            return [
                False,
                "One of the sales does not have vol obs. Please check before uploading again.",
            ]
        elif selling_price == None:
            return [
                False,
                "One of the sales does not have selling price. Please check before uploading again.",
            ]
        elif type(vol_obs) == str:
            return [False, vol_obs]
        elif type(vol_20) == str:
            return [False, vol_20]

        customers = Customer.objects.filter(name=customer)
        if customers.exists():
            customer = customers.last()
        else:
            return [
                False,
                "The customer you enter in one of the sales does not exist. Make sure you select the customer from the dropdown list.",
            ]

        products = Product.objects.filter(name=product)
        if products.exists():
            product = products.last()
        else:
            return [
                False,
                "The product you entered in one of the sales does not exist. Make sure you select the product from the dropdown list.",
            ]

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
                        customer=customer, plate_no=truck, driver=driver
                    )
            sales = Sale.objects.filter(order_no=order_no)
            if not sales.exists():
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
                    loading_date=loading_date,
                    remarks=remarks,
                )
        else:
            if type(date) == str or type(loading_date) == str:
                return [
                    False,
                    "Check your dates they appear as strings. You can fix it by selecting the date column. Then press ctrl+1. select date the 14-07-12 format.",
                ]

            trucks = Truck.objects.filter(plate_no=truck)
            if trucks.exists():
                truck = trucks.last()
            else:
                driver = Driver(name=driver)
                truck = Truck(plate_no=truck, driver=driver)
            sales = Sale.objects.values("order_no").filter(order_no=order_no)
            if sales.exists():
                return [
                    False,
                    f"Order no: {order_no} is already in the system. Please check the sale record.",
                ]

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
                loading_date=loading_date,
                remarks=remarks,
            )
        return [True, "File Uploaded Successful"]

    except Exception as e:
        print(e)
        return [False, "An unknown error occured. Contact the admin"]


def up(reader, depot, save):
    order_nos = []
    for row in reader:
        if row[5] in order_nos:
            return [False, "Two sales have the same order no. Please check"]
        if row[0] != None and row[1] != None and row[2] != None:
            succesful = upload(row, depot, save=save)
            if not succesful[0]:
                return [False, succesful[1]]
        order_nos.append(row[5])
    return [True, "File uploaded successful"]


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
            if succesful[0] == False:
                return Response(
                    {
                        "status": "fail",
                        "message": succesful[1],
                    }
                )
            HandleExcelUpload(reader, depot).start()

            return Response({"status": "success", "message": "Uploaded successful"})
        else:

            return Response(
                {
                    "status": "fail",
                    "message": "Make sure the file used is has correct headers as the template. Do not add any new column",
                }
            )
