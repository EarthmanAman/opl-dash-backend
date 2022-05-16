from django.db import models
from django.contrib.auth.models import User

class Depot(models.Model):

    # Attributes
    name    = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class DepotManager(models.Model):

    # Relations
    depot   = models.ForeignKey(Depot, on_delete=models.PROTECT)
    user    = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.user.first_name + " : " + self.depot.name
