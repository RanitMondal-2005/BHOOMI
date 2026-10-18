# crops/models.py
from django.db import models


# this model stores the pre filled reference data for each crop
class CropProfile(models.Model):

    crop_name = models.CharField(max_length=50, unique=True)

    # soil type is stored as text with comma separated values
    # example: "Loamy, Sandy Loam"
    # we are keeping it simple as text instead of a separate table for now
    suitable_soil_types = models.CharField(max_length=200)

    # soil level parameters, these come from our sensors
    ph_min = models.FloatField()
    ph_max = models.FloatField()

    moisture_min = models.FloatField()  # in percentage
    moisture_max = models.FloatField()

    nitrogen_min = models.FloatField()  # mg/kg
    nitrogen_max = models.FloatField()

    phosphorus_min = models.FloatField()  # mg/kg
    phosphorus_max = models.FloatField()

    potassium_min = models.FloatField()  # mg/kg
    potassium_max = models.FloatField()

    ec_min = models.FloatField()  # electrical conductivity, dS/m
    ec_max = models.FloatField()

    soil_temp_min = models.FloatField()  # degree celsius
    soil_temp_max = models.FloatField()

    # environmental parameters, these come from DHT11 (ambient, not soil)
    ambient_temp_min = models.FloatField()
    ambient_temp_max = models.FloatField()

    humidity_min = models.FloatField()  # percentage
    humidity_max = models.FloatField()

    # this controls how the crop name shows up in django admin and anywhere we print the object
    def __str__(self):
        return self.crop_name
