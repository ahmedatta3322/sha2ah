
from django.db import models
from django.urls import reverse


# Create your models here.
class Contract(models.Model):
    type = models.CharField(choices=[('rent','rent'),('investment' , 'investment')], max_length=50)
    unit = models.ForeignKey("estate.Unit", on_delete=models.CASCADE)
    beneficiary_name = models.TextField()
    rent_cost = models.IntegerField()
    rent_ferquency = models.CharField(choices=[('monthly','rent'),('yearly' , 'investment')], max_length=50)
    contract_holder_name = models.TextField()
    date_from = models.DateField(auto_now=False, auto_now_add=False)
    date_to = models.DateField(auto_now=False, auto_now_add=False)
    first_rent_due_date = models.DateField(auto_now=False, auto_now_add=False)
    notes = models.TextField()
class Document(models.Model):
    contract = models.ForeignKey("Contract",  on_delete=models.CASCADE)
    type = models.CharField(choices=[('rent','rent'),('investment' , 'investment')], max_length=50)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
