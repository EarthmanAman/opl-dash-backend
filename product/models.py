from django.db import models

class Product(models.Model):
    
    # Attributes
    name    = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
