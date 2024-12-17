from django.core.exceptions import ValidationError
from django.db import models
from models import Comarca, Municipios

################## Fomracion ####################
def validar_longitud_nueve(value): 
    if len(str(value)) != 9: 
        raise ValidationError('El número debe tener exactamente 9 dígitos.')

######## familia porfesional ######
class Familia_Profesion(models.Model):
    pk_fm_pro= models.CharField(max_length=20,verbose_name="id de Entidad Formadora",primary_key=True)
    desc_fm_pro= models.CharField(max_length=200, verbose_name="Descripcion de la Familia Profesional")
    def __str__(self):
        return f"{self.pk_fm_pro}"
    class Meta:
        db_table = "Familia_Profesional" 

class Estudio_Profesion(models.Model):
    pk_est_pro= models.CharField(max_length=20,verbose_name="id de Estudio Profecional",primary_key=True)
    desc_est_pro= models.CharField(max_length=220, verbose_name="Descripcion de la Estudio Profesional")
    def __str__(self):
        return f"{self.pk_est_pro}"
    class Meta:
        db_table = "Estudio_Profesional" 

######## Entidad Formadora ###### tabla Origen de datos foap2024
##7 Entidad Formadora -> Ent_For 
class Ent_For(models.Model):
    pk_ent_for= models.CharField(max_length=20,verbose_name="id de Entidad Formadora",primary_key=True)
    nom_ent_for= models.CharField(max_length=44, verbose_name="nombre de Entidad Formadora")
    Area_for_ent_for= models.CharField(max_length=44,verbose_name="area de formacion de Entidad Formadora")
    email_ent_for= models.EmailField(verbose_name="correo de la entidad")
    nif_ent_for= models.CharField(max_length=20,verbose_name="NIF de Entidad Formadora")
    fec_fin_ent_for= models.DateField(verbose_name="Fecha de fin")
    fec_ini_ent_for= models.DateField(verbose_name="Fecha de inicio")
    area_prof_ent_for= models.CharField(max_length=44,verbose_name="Area Porfecional de Entidad Formadora")
    cm_ent_for= models.CharField(max_length=5,verbose_name="Codigo del municipio de Entidad Formadora")
    web_ent_for =models.CharField (max_length=100,verbose_name="link de la web de Entidad Formadora") 
    horas_ent_for= models.IntegerField(verbose_name="horas de la Entidad Formadora")
    idt_ent_for= models.IntegerField(verbose_name="identificador de la Entiad Formadora")
    den_ent_for= models.CharField (max_length=100,verbose_name="Denominacion de Entidad Formadora")
    amb_ent_for= models.CharField (max_length=100,verbose_name="Ambito de Entidad Formadora")
    mod_ent_for= models.CharField (max_length=50,verbose_name="Modalidad de Entidad Formadora")
    num_grupo= models.IntegerField(verbose_name="Numero de grupo de la Entidad Formadora")
    telefono= models.CharField (
        max_length=15,
        validators=[validar_longitud_nueve],
        verbose_name="telefono de Entidad Formadora"
        )
    fk_mun_ent_for = models.ForeignKey(Municipios, on_delete=models.CASCADE, related_name='Municipios') #cod_municipo (nom_municipio,) ok
    fk_com_ent_for = models.ForeignKey(Comarca, on_delete=models.CASCADE, related_name='Comarca') #cd_comarca (nom_comarca) ok
    fk_fam_pro =models.ForeignKey(Familia_Profesion, on_delete=models.CASCADE, related_name='Familia_Profesion')

    def __str__(self):
        return f"{self.nom_ent_for}"
    class Meta:
        db_table = "Ent_For" 


