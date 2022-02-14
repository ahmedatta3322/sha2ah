from django.contrib import admin

from estate.models import Estate, Unit

from . import models


# Register your models here.
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    exclude = ()

