from django.db import models
from django.db.models.base import Model
from django.urls import reverse
# Create your models here.
class Invoice(models.Model):
    unit = models.ForeignKey("estate.Unit", on_delete=models.CASCADE)
    statulist = [
        ('pending','pending'),
        ('paid','paid'),
        ('paid','paid'),
        ('late','late'),
        ('due','due'),
        ('upcoming','upcoming'),
        ('canceled','canceled')
        ]
    status = models.CharField(choices=statulist, max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    payment_method = models.CharField(choices=[("fawry" ,"fawry")], max_length=50)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
