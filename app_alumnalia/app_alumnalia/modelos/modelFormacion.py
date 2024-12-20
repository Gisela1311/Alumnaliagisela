from django.core.exceptions import ValidationError
from django.db import models
from .modelDir import Comarca, Provincias, Municipios

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

class Denominacion(models.Model):
    pk_deno= models.CharField(max_length=20,verbose_name="id de Denominacion",primary_key=True)
    desc_den= models.CharField(max_length=200, verbose_name="Descripcion de la Denominacion")
    def __str__(self):
        return f"{self.pk_den}"
    class Meta:
        db_table = "Denominacion" 

class Ambito(models.Model):
    pk_amb= models.CharField(max_length=20,verbose_name="id de Ambito",primary_key=True)
    desc_amb= models.CharField(max_length=200, verbose_name="Descripcion del Ambito")
    def __str__(self):
        return f"{self.desc_amb}"
    class Meta:
        db_table = "Ambito" 

class Estudio_Profesion(models.Model):
    pk_est_pro= models.CharField(max_length=20,verbose_name="id de Estudio Profecional",primary_key=True)
    desc_est_pro= models.CharField(max_length=220, verbose_name="Descripcion de la Estudio Profesional")
    def __str__(self):
        return f"{self.desc_est_pro}"
    class Meta:
        db_table = "Estudio_Profesional" 

######## Entidad Formadora ###### tabla Origen de datos foap2024
#1
def validar_longitud_nueve(value): 
    if len(str(value)) != 9: 
        raise ValidationError('El número debe tener exactamente 9 dígitos.')

####### Escuela
class Escuela(models.Model):
    pk_esc= models.CharField(max_length=20,verbose_name="id de Entidad Formadora",primary_key=True)
    nom_esc= models.CharField(max_length=44, verbose_name="nombre de Entidad Formadora")
    email_esc= models.EmailField(verbose_name="correo de la entidad")
    nif_esc= models.CharField(max_length=20,verbose_name="NIF de Entidad Formadora")    
    web_esc =models.CharField (max_length=100,verbose_name="link de la web de Entidad Formadora") 
    tel_esc= models.CharField (
        max_length=15,
        validators=[validar_longitud_nueve],
        verbose_name="telefono de Entidad Formadora"
        )
    def __str__(self):
        return f"{self.nom_esc}"
    class Meta:
        db_table = "Escuela" 
#2
#### Calemndario
class Calendario(models.Model):
    pk_cal = models.IntegerField(
        verbose_name="id de Calendario",
        primary_key=True
        ) 
    dat_ini_cal = models.DateField(verbose_name="Fecha de inicio del curso")
    dat_fin_cal = models.DateField(verbose_name="Fecha de fin del curso")    
    nom_grup_cal =  models.CharField(max_length=30, verbose_name="Numero de grupo asignado en el calendario")
    def __str__(self):
        return f"{self.nom_grup_cal}"
    class Meta:
        db_table = "Calendario" 

#3
class Cusrso(models.Model):
    pk_cal= models.CharField(max_length=20,verbose_name="id de Curso",primary_key=True)
    idt_ent_for= models.IntegerField(verbose_name="identificador de la Entiad Formadora")
    area_prof_ent_for= models.CharField(max_length=44,verbose_name="Area Porfecional de Entidad Formadora")
    fk_fam_pro =models.ForeignKey(Familia_Profesion, on_delete=models.CASCADE, related_name='Cusrso')
    fk_den_for =models.ForeignKey(Denominacion, on_delete=models.CASCADE, related_name='Denomincion')
    fk_amb_for= models.ForeignKey(Ambito, on_delete=models.CASCADE, related_name='Ambito',verbose_name="Ambito de Entidad Formadora")
    horas_ent_for= models.TimeField(null=True, blank=True,verbose_name="horas de la Entidad Formadora")
    modalidad = [
        ('', 'Seleccione una opción'),
        ('1', 'Presencial'),
        ('2', 'En línea'),
        ('3', 'Mixta')
    ]
    mod_cur= models.CharField(
        verbose_name="Modalidad de estudio",
        choices=modalidad,
        default='', 
        max_length=1
    )
    def __str__(self):
        return f"{self.area_prof_ent_for}"
    class Meta:
        db_table = "Curso" 

class Oferta_Formativa(models.Model):
    pk_Ofe_for= models.CharField(max_length=20,verbose_name="id de Oferta Formadora",primary_key=True)
    nom_ofe= models.CharField(max_length=44, verbose_name="nombre de la oferta")
    Area_for_ent_for= models.CharField(max_length=44,verbose_name="Area de formacion de la oferta")
    fk_esc_pro =models.ForeignKey(Escuela, on_delete=models.CASCADE, related_name='Escuela')
    fk_cal =models.ForeignKey(Calendario, on_delete=models.CASCADE, related_name='Escuela')
    fk_cur =models.ForeignKey(Cusrso, on_delete=models.CASCADE, related_name='Escuela')
    fk_pro =models.ForeignKey(Provincias, on_delete=models.CASCADE, related_name='Escuela')
    fk_mun =models.ForeignKey(Municipios, on_delete=models.CASCADE, related_name='Escuela')
    fk_com =models.ForeignKey(Comarca, on_delete=models.CASCADE, related_name='Escuela')
    def __str__(self):
        return f"{self.nom_ofe}"
    class Meta:
        db_table = "Oferta_Formativa" 

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
    fk_mun_ent_for = models.ForeignKey(Municipios, on_delete=models.CASCADE, related_name='Municipios') 
    fk_com_ent_for = models.ForeignKey(Comarca, on_delete=models.CASCADE, related_name='Comarca') 
    fk_fam_pro =models.ForeignKey(Familia_Profesion, on_delete=models.CASCADE, related_name='Familia_Profesion')

    def __str__(self):
        return f"{self.nom_ent_for}"
    class Meta:
        db_table = "Ent_For" 


