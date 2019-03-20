import uuid
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Site(BaseModel):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    description = models.TextField()
    justification = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    area_hectares = models.FloatField(null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    state = models.ForeignKey('States', on_delete=models.CASCADE, null=True)
    iso = models.ForeignKey('Iso', on_delete=models.CASCADE, null=True)
    region = models.ForeignKey('Region', on_delete=models.CASCADE, null=True)

class Category(BaseModel):
    name = models.CharField(max_length=128)

class States(BaseModel):
    name = models.CharField(max_length=128)
    
class Iso(BaseModel):
    name = models.CharField(max_length=2)

class Region(BaseModel):
    name = models.CharField(max_length=128)