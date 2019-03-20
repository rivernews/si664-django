from django.contrib import admin
from cats.models import Cat, Breed

# Register your models here.
@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'weight', 'foods', 'breed')

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('name',)