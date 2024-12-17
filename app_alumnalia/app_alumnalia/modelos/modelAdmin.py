from django.core.exceptions import ValidationError
from django.db import models
################## Administracio ####################

class Tipo_Usuario(models.Model):
    pk_tip_user= models.CharField(max_length=20,verbose_name="id de tip de usurio",primary_key=True)
    nom_tip_user= models.CharField(max_length=10, verbose_name="Descripcion del tipo de usuario")
    per_tip_user= models.SmallIntegerField(max_length=2, verbose_name="permiso del tipo de usuario")
    def __str__(self):
        return f"{self.nom_tipo_user}"
    class Meta:
        db_table = "Tipo_Usuario" 