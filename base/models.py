from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    common_name = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    organization_unit_name = models.CharField(max_length=50)
    locality = models.CharField(max_length=50)
    state_name = models.CharField(max_length=50)
    country_name = models.CharField(max_length=2)
    email = models.EmailField()

    def __str__(self):
        return self.common_name
