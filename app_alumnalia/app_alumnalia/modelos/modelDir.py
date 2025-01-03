from django.core.exceptions import ValidationError
from django.db import models
################# direcciones del sistema ########################
######## Direcciones ######
#1 tabla de la Comarca
class Comarca(models.Model):
    pk_com = models.SmallIntegerField(
        verbose_name="id de Comarca",
        primary_key=True
        ) 
    nom_com =  models.CharField(max_length=30, verbose_name="nombre de la Comarca")
    def __str__(self):
        return f" {self.pk_com} : {self.nom_com}"
    class Meta:
        db_table = "Comarca" 
        ordering = ['pk_com']

#2 tabla de la Provincias
class Municipios(models.Model):
    pk_mun = models.IntegerField(
        verbose_name="id de Municipios", 
        primary_key=True
        ) 
    nom_mun =  models.CharField(max_length=30, verbose_name="nombre de la Municipios")
    fk_com = models.ForeignKey(Comarca, on_delete=models.CASCADE, related_name='Municipios')
    def __str__(self):
        return f"id: {self.pk_mun} nombre: {self.nom_mun}"
    class Meta:
        db_table = "Municipios" 

#3 tabla de la Provincias
class Provincias(models.Model):
    pk_pro = models.SmallIntegerField( #SmallAutoField
        verbose_name="id de Provincias", 
        primary_key=True
        ) 
    nom_pro =  models.CharField(max_length=30, verbose_name="nombre de la Provincia")
    def __str__(self):
        return f"{self.nom_pro}"
    class Meta:
        db_table = "Provincias" 

#4 tabla de la Provincias
class Comarca_provincias(models.Model):
    pk_cam_pro = models.SmallIntegerField( #SmallAutoField
        verbose_name="id de Comarca_provincias", 
        primary_key=True
        )     
    fk_com = models.ForeignKey(Comarca, on_delete=models.CASCADE, verbose_name="id de la Comarca", related_name='Comarca_provincias', default=True)
    fk_pro = models.ForeignKey(Provincias, on_delete=models.CASCADE,  verbose_name="id de la Provicia", related_name='Comarca_provincias', default=True)
    def __str__(self):
        return f"{self.pk_cam_pro} : {self.fk_com} : {self.fk_pro}"
    class Meta:
        db_table = "Comarca_provincias" 
        ordering = ['fk_com']

class TipoVia(models.Model): 
    pk_via = models.SmallIntegerField( #SmallAutoField
        verbose_name="id de Tipo de Via", 
        primary_key=True        
        ) 
    nom_via = models.CharField(
            max_length=100, 
            verbose_name="Tipo de via"
        ) 
    def __str__(self): 
        return self.nom_via
    class Meta:
        db_table= "TipoVia"


######### Area de Vistas de las Direciones ##################

class MisDirecciones(models.Model): 
    class Meta: managed = False 
    db_table = 'Direcciones'  #view_consultar_recetas
    pk_com = models.AutoField(primary_key=True) 
    nom_com = models.CharField(max_length=30, verbose_name="nombre de la Comarca")
    pk_pro = models.SmallIntegerField(verbose_name="id de Provincias") 
    nom_pro = models.CharField(max_length=30, verbose_name="nombre de la Provincia")
    pk_mun = models.IntegerField(verbose_name="id de Municipios") 
    nom_mun = models.CharField(max_length=30, verbose_name="nombre de la Municipios")

    def __str__(self):
        return f"{self.pk_com}"
    class Meta:
        db_table = "MisDirecciones" 