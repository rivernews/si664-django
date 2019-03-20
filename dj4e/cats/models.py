from django.db import models

from django.urls import reverse
from django.core.validators import MinLengthValidator

# Create your models here.
class Cat(models.Model):
    nickname = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
    )

    weight = models.PositiveIntegerField()
    foods = models.CharField(max_length=300)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['nickname']
        permissions = (
            ('CatFullAccess', 'Full access: can do CRUD on cat'),
            ('CatReadOnly', 'Read only: can read all cat data, but not modifying them'),
        )

    def get_absolute_url(self):
        return reverse('cat', args=[str(self.id)])
    
    def __str__(self):
        return self.nickname

class Breed(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Breed must be greater than 1 character")]
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('breed', args=[str(self.id)])
    
    class Meta:
        ordering = ['name']
        permissions = (
            ('BreedFullAccess', 'Full access: can do CRUD on breed'),
            ('BreedReadOnly', 'Read only: can read all breed data, but not modifying them'),
        )