from django.db import models

# Create your models here.
class Estate(models.Model):
    name = models.TextField()
    type = models.CharField(choices=[("residential" , "residential")], max_length=50)
    number_of_floors = models.IntegerField()
    units_per_floor = models.IntegerField()
class Unit(models.Model):
    name = models.TextField()
    phone = models.PhoneNumberField()
    estate = models.ForeignKey("Estate", on_delete=models.CASCADE)
    floor = models.IntegerField()
    number = models.IntegerField()