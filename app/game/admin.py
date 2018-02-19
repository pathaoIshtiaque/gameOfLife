from django.contrib import admin
from .models import Grid

class GridAdmin(admin.ModelAdmin):
    pass
admin.site.register(Grid, GridAdmin)
# Register your models here.
