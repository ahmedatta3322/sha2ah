from pyexpat import model
from statistics import mode
from django.db import models


# Create your models here.
class Estate(models.Model):
    name = models.TextField()
    # estate_type = models.CharField(choices=[("residential" , "residential")], max_length=50)
    number_of_floors = models.IntegerField()
    units_per_floor = models.IntegerField()
    estate_type = models.ForeignKey("estate.EstateType", on_delete=models.PROTECT ,default=1)
    def __str__(self) -> str:
        return self.name
class Unit(models.Model):
    name = models.TextField()
    phone = models.TextField()
    estate = models.ForeignKey("Estate", on_delete=models.CASCADE)
    floor = models.IntegerField()
    number = models.IntegerField()
    def __str__(self) -> str:
        return self.name
class EstateType(models.Model):
    name = models.CharField(max_length=50)
    
