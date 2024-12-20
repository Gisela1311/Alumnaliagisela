from django.core.exceptions import ValidationError
from django.db import models
################## Actividad Economica ####################







###### cursos
#"__id", "identificador", "area_professional", "familia_professional","denominacio","ambit", "hores", "modalitat"
"""
class Curso(models.Model):
    pk_cur = models.SmallIntegerField(
        verbose_name="id de escuela",
        primary_key=True
        ) 
    identificador
    area_professional
    familia_professional
    denominacio
    ambit
    hores
    modalitat
    email_esc = models.EmailField(verbose_name="Email de la entidad")
    nif_esc = models.CharField(max_length=15, unique=True, verbose_name="NIF de la Entidad", null=False)
    nom_esc =  models.CharField(max_length=30, verbose_name="nombre de la entidad")
    web_esc =  models.CharField(max_length=30, verbose_name="web de la entidad")
    tel_per = models.IntegerField(verbose_name="Teléfono", validators=[validar_longitud_nueve])
    def __str__(self):
        return f"{self.nom_esc}"
    class Meta:
        db_table = "Escuela" 
"""