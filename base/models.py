from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    bio = models.CharField(max_length=1000)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name