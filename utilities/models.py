from django.db import models
#from django.db.models.base import Model

# Create your models here.
class City(models.Model):
    name = models.TextField()
    code = models.TextField()
    call_code = models.IntegerField()
    government = models.ForeignKey("Government", on_delete=models.CASCADE)   
    country = models.ForeignKey("Country", on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name
class Country(models.Model):
    name = models.TextField()
    code = models.TextField()
    call_code = models.IntegerField()
    def __str__(self) -> str:
        return self.name
class Government(models.Model):
    name = models.TextField()
    code = models.TextField()
    call_code = models.IntegerField()
    country = models.ForeignKey("Country", on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name
class Address(models.Model):
    type = models.CharField(choices = [("trade" , 'trade') , ("resdential",'resdential')] , max_length=100)
    street = models.TextField()
    building = models.TextField()
    area = models.TextField()
    country = models.ForeignKey("Country", on_delete=models.CASCADE)
    government = models.ForeignKey("Government", on_delete=models.CASCADE)
    city = models.ForeignKey("City", on_delete=models.CASCADE)
    long = models.TextField()
    lat = models.TextField()
    def __str__(self) -> str:
        return self.name
class Currency(models.Model):
    country = models.ForeignKey("Country", on_delete=models.CASCADE)
    code = models.TextField()
    def __str__(self) -> str:
        return self.name