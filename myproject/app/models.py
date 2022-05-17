from django.db import models


# Create your models here.
class MyModel(models.Model):
    field1 = models.CharField(default="1", max_length=255)
    field2 = models.CharField(default="1", max_length=255)
    field3 = models.CharField(default="1", max_length=255)
