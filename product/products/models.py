from django.db import models
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    launch_date=models.DateField()
    def __str__(self) -> str:
        return f"{Product.name}"
# Create your models here.
