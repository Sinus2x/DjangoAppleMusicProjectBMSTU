from django.db import models


class Albums(models.Model):
    album_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15, db_column='name')
    n_songs = models.IntegerField()
    artist = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'albums'


class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING)
    album = models.ForeignKey(Albums, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orders'
