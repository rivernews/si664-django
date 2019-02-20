from django.contrib import admin
from autos.models import Auto, Make

# Register your models here.
@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'make',)

@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ('name',)
