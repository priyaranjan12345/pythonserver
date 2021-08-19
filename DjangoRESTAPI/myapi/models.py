from django.db import models

# Create your models here.
class Cars(models.Model):
    car_name = models.CharField(max_length=100)
    car_price = models.IntegerField()
    fuel_type = models.CharField(max_length=100)
    car_feature = models.CharField(max_length=100)

    def __str__(self):
        return self.car_name