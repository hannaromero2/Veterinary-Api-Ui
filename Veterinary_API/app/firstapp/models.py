from django.db import models

# Create your models here.


class Servicios(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    banio = models.CharField(max_length=45)
    corte = models.CharField(max_length=45)
    arreglo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'servicios'

class Pet(models.Model):
    id_pet = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=False)
    breed = models.CharField(max_length=45, blank=True, null=True)
    age = models.CharField(max_length=45, blank=True, null=False)
    owner_id = models.IntegerField(blank=True, null=True)
    body_color = models.CharField(max_length=45,blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True)
    pet_type = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'pet'

class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=45)
    phone = models.IntegerField(max_length=45)
    address = models.IntegerField(max_length=45, null=True)

    class Meta:
        managed = False
        db_table = 'owner'