from django.db import models
from django.urls import reverse
# Create your models here.
class Wallet(models.Model):
    total = models.IntegerField()
    total_offline_collected = models.IntegerField()
    total_online_collected = models.IntegerField()
    total_pending = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
