# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#from django.db import models




class AsinsToTrack(models.Model):
    asin_id = models.AutoField(primary_key=True)
    asin = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    tracking_active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asins_to_track'



class StockRecords(models.Model):
    stock_record_id = models.AutoField(primary_key=True)
    asin = models.ForeignKey(AsinsToTrack, models.DO_NOTHING, blank=True, null=True)
    asin_0 = models.CharField(db_column='asin', max_length=100)  # Field renamed because of name conflict.
    stock_amount = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_records'
