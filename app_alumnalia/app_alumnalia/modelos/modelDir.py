from django.core.exceptions import ValidationError
from django.db import models
################# direcciones del sistema ########################
######## Direcciones ######
#1 tabla de la Comarca
class Comarca(models.Model):
    pk_com = models.SmallAutoField(
        verbose_name="id de Comarca",
        primary_key=True
        ) 
    nom_com =  models.CharField(max_length=30, verbose_name="nombre de la Comarca")
    def __str__(self):
        return f"{self.nom_com}"
    class Meta:
        db_table = "Comarca" 

#2 tabla de la Provincias
class Municipios(models.Model):
    pk_mun = models.SmallAutoField(
        verbose_name="id de Municipios", 
        primary_key=True
        ) 
    nom_mun =  models.CharField(max_length=30, verbose_name="nombre de la Municipios")
    fk_com = models.ForeignKey(Comarca, on_delete=models.CASCADE, related_name='Municipios')
    def __str__(self):
        return f"{self.nom_mun}"
    class Meta:
        db_table = "Municipios" 

#3 tabla de la Provincias
class Provincias(models.Model):
    pk_pro = models.SmallAutoField(
        verbose_name="id de Provincias", 
        primary_key=True
        ) 
    nom_pro =  models.CharField(max_length=30, verbose_name="nombre de la Provincia")
    def __str__(self):
        return f"{self.pk_pro}"
    class Meta:
        db_table = "Provincias" 

#4 tabla de la Provincias
class Comarca_provincias(models.Model):
    pk_cam_pro = models.SmallAutoField(
        verbose_name="id de Comarca_provincias", 
        primary_key=True
        )     
    fk_com = models.ForeignKey(Comarca, on_delete=models.CASCADE, related_name='Comarca_provincias')
    fk_pro = models.ForeignKey(Provincias, on_delete=models.CASCADE, related_name='Comarca_provincias')
    def __str__(self):
        return f"{self.pk_pro}"
    class Meta:
        db_table = "Comarca_provincias" 

