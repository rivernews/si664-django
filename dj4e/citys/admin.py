from django.contrib import admin
from citys.models import City, State

# Register your models here.
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'population', 'slogan', 'state')

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name',)