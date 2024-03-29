# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Houses(models.Model):
    id = models.TextField(blank=True, null=False, primary_key=True)
    date = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    bedrooms = models.TextField(blank=True, null=True)
    bathrooms = models.TextField(blank=True, null=True)
    sqft_living = models.TextField(blank=True, null=True)
    sqft_lot = models.TextField(blank=True, null=True)
    floors = models.TextField(blank=True, null=True)
    waterfront = models.TextField(blank=True, null=True)
    view = models.TextField(blank=True, null=True)
    condition = models.TextField(blank=True, null=True)
    grade = models.TextField(blank=True, null=True)
    sqft_above = models.TextField(blank=True, null=True)
    sqft_basement = models.TextField(blank=True, null=True)
    yr_built = models.TextField(blank=True, null=True)
    yr_renovated = models.TextField(blank=True, null=True)
    zipcode = models.TextField(blank=True, null=True)
    lat = models.TextField(blank=True, null=True)
    long = models.TextField(blank=True, null=True)
    sqft_living15 = models.TextField(blank=True, null=True)
    sqft_lot15 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'houses'
