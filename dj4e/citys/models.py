from django.db import models

from django.urls import reverse
from django.core.validators import MinLengthValidator

# Create your models here.
class City(models.Model):
    nickname = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
    )

    population = models.PositiveIntegerField()
    slogan = models.CharField(max_length=300)
    state = models.ForeignKey('State', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['nickname']
        permissions = (
            ('CityFullAccess', 'Full access: can do CRUD on city'),
            ('CityReadOnly', 'Read only: can read all city data, but not modifying them'),
        )

    def get_absolute_url(self):
        return reverse('city', args=[str(self.id)])
    
    def __str__(self):
        return self.nickname

class State(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "State must be greater than 1 character")]
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('state', args=[str(self.id)])
    
    class Meta:
        ordering = ['name']
        permissions = (
            ('StateFullAccess', 'Full access: can do CRUD on state'),
            ('StateReadOnly', 'Read only: can read all state data, but not modifying them'),
        )