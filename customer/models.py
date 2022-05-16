from operator import mod
from django.db import models

class Customer(models.Model):

    # Attributes
    name    = models.CharField(max_length=100)
    code    = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.code + " : " + self.name

class Driver(models.Model):

    # Attributes
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.first_name

class Truck(models.Model):

    # Relations
    driver      = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)

    # Attributes
    plate_no    = models.CharField(max_length=20)
    is_hired    = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.driver.__str__() + " : " + self.plate_no

