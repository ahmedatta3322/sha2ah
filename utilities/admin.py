from django.contrib import admin

from utilities import models
# Register your models here.

admin.site.register(models.Address)
admin.site.register(models.Country)
admin.site.register(models.City)
admin.site.register(models.Government)
admin.site.register(models.Currency)

