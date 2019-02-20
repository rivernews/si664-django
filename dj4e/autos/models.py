from django.db import models

from django.urls import reverse

# Create your models here.
class Auto(models.Model):
    nickname = models.CharField(max_length=100)
    make = models.ForeignKey('Make', on_delete=models.SET_NULL, null=True)
    mileage = models.PositiveIntegerField(default=0)
    comments = models.CharField(max_length=300, null=True)

    class Meta:
        ordering = ['make']
        permissions = (
            ('AutoFullAccess', 'Full access: can do CRUD on auto'),
            ('AutoReadOnly', 'Read only: can read all auto data, but not modifying them'),
        )

    def get_absolute_url(self):
        return reverse('auto', args=[str(self.id)])
    
    def __str__(self):
        return self.nickname

class Make(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        permissions = (
            ('MakeFullAccess', 'Full access: can do CRUD on make'),
            ('MakeReadOnly', 'Read only: can read all make data, but not modifying them'),
        )

    def get_absolute_url(self):
        return reverse('make', args=[str(self.id)])
    
    def __str__(self):
        return self.name