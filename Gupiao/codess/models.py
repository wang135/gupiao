# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class RidayProducts11(models.Model):
    time = models.CharField(max_length=255, blank=True, null=True)
    opens = models.CharField(max_length=255, blank=True, null=True)
    closes = models.CharField(max_length=255, blank=True, null=True)
    high = models.CharField(max_length=255, blank=True, null=True)
    low = models.CharField(max_length=255, blank=True, null=True)
    volume = models.CharField(max_length=255, blank=True, null=True)
    volumemoney = models.CharField(max_length=255, blank=True, null=True)
    huanshou = models.CharField(max_length=255, blank=True, null=True)
    names = models.CharField(max_length=255, blank=True, null=True)
    codes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'riday_products11'
