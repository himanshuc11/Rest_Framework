from django.db import models

# Create your models here.
class People(models.Model):
    first = models.CharField(max_length=128)
    last = models.CharField(max_length=128)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first} {self.last}"