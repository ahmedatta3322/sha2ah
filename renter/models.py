import imp
from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.db import models
from django.core.mail import send_mail

from django.utils.translation import ugettext_lazy as _


class Renter(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    name = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = PhoneField(blank=False, help_text="Contact phone number")

    def __str__(self) -> str:
        return super().__str__()
