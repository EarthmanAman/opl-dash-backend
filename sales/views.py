from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

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
        entries = Sale.objects.all().select_related()
        serializer = RetrieveSaleSer(entries, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CreateSaleSer(data=request.data)

        if serializer.is_valid():
            sale = serializer.save()
            serializer = RetrieveSaleSer(sale)
            return Response(serializer.data)
        else:
            print(serializer.errors)


class RetrieveSaleView(RetrieveUpdateAPIView):
    serializer_class = RetrieveSaleSer
    queryset = Sale.objects.all()


class UploadExcel(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        sale_resource = SaleResource()
        dataset = Dataset()
        file = request.FILES["file"]
        r = file.read()
        print(r)
        imported_data = dataset.load(r)
        result = sale_resource.import_data(
            dataset, dry_run=True
        )  # Test the data import
        if not result.has_errors():
            # sale_resource.import_data(dataset, dry_run=False)  # Actually import now
            return Response(
                {"status": status.HTTP_201_CREATED, "message": "Upload successful"}
            )
        return Response(
            {
                "status": status.HTTP_403_FORBIDDEN,
                "message": "Check your file format. If error persist contact admin",
            }
        )
