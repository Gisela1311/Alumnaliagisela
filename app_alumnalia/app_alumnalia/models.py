from django.core.exceptions import ValidationError
from django.db import models

def validar_dni(value): 
    if not value.isalnum() or len(value) != 9: 
        raise ValidationError("El DNI debe tener 9 caracteres alfanuméricos.")

# Tabla de Datos Personales

class Dat_Per(models.Model):
    pk_per = models.SmallAutoField(verbose_name="id de la Dat_Per", primary_key=True) 
    nom_per = models.CharField(max_length=150, verbose_name="Nombre de la Persona", null=False)    
    dni_per = models.CharField(max_length=15, unique=True, verbose_name="Nombre de la autoridad", validators=[validar_dni], null=False)
    fn_per = models.DateField(verbose_name="fecha de nacimiento de la persona")
    cn_per = models.CharField(max_length=150, verbose_name="Naciuonalidad de la persona", null=False)    
    tel_per = models.IntegerField(verbose_name="Teléfono de la persona", null=True)
    email_per = models.EmailField(verbose_name="email de la persona")
    dir_per = models.CharField(max_length=150, verbose_name="Dirección de la persona", null=False) #models.ForeignKey(  on_delete=models.CASCADE, verbose_name="Dirección de la persona", default=0) #Direcciones
    sex_per = models.CharField(max_length=150, verbose_name="genero de la persona", null=False)
    # Si se acepta o no la Declaraciones y Consentimientos de sus datos
    uso_datos_per = models.BooleanField(verbose_name="fines de gestión académica y administrativa",default=True)
    term_per = models.BooleanField(verbose_name="términos y condiciones",default=True)
    noti_per = models.BooleanField(verbose_name="notificaciones de oportunidades formativas",default=True)
    def __str__(self):
        return f"{self.nom_per}"
    class Meta:
        db_table = "Dat_Per"

# tabla de la Información Profesional
class Inf_Prof(models.Model):
    pk_inf_pro = models.SmallAutoField(verbose_name="id de la Información Profesional", primary_key=True) 
    #models.IntegerField(min_value=0, max_length=2, min_length=2, verbose_name="id de la Información Profesional", primary_key=True) 

    Titulo = [ 
        ('1', 'Técnico/a'), 
        ('2', 'Grado universitario'), 
        ('3', 'Máster'), 
        ('4', 'Doctorado'), 
        ('5', 'Doctorado'), 
        (6, 'especificar'), #Otro (especificar)
        ]    

    tit_inf_pro = models.IntegerField(
        max_length=2,
        verbose_name="Título académico más alto obtenido",
        choices=Titulo, 
        default='1'
        )  
    tit_esp_inf_pro = models.CharField(
        max_length=15, 
        verbose_name="especificar tit_inf_pro"

        )  

    esp_inf_pro = models.CharField(max_length=15,verbose_name="En qué área está tu especialización principal")  

    exp_inf_pro = models.CharField(max_length=15,verbose_name="Cuántos años de experiencia tienes como formador/a")  
    for_imp_inf_pro = models.CharField(max_length=15,verbose_name="Qué tipo de formación has impartido")  
    cv_adj_inf_pro = models.CharField(max_length=15,verbose_name="Adjunta tu currículum en formato PDF.")  
    
    mod_inf_pro = models.CharField(max_length=15,verbose_name="Qué modalidades de enseñanza prefieres impartir")  
    tipo_alu_inf_pro = models.CharField(max_length=15,verbose_name="Qué tipo de alumnado prefieres formar")  
    tipo_alu_esp_inf_pro = models.CharField(max_length=15, verbose_name="especificar")  
    
    franja_inf_pro = models.CharField(max_length=15,verbose_name="En qué franjas horarias estás disponible para impartir clases")  

    cert_inf_pro = models.CharField(max_length=15,verbose_name="Tienes alguna certificación docente")  
    cert_esp_inf_pro = models.CharField(max_length=15, verbose_name="especificar")  

    herr_inf_pro = models.CharField(max_length=15,verbose_name="Qué herramientas tecnológicas utilizas en tus clases")  
    herr_esp_inf_pro = models.CharField(max_length=15, verbose_name="especificar")

    comp_dig_inf_pro = models.CharField(max_length=15,verbose_name="Posees competencias digitales específicas ej. DigCompEdu")  
    comp_dig_esp_inf_pro = models.CharField(max_length=15, verbose_name="especificar")

    fk_per_inf_pro =  models.ForeignKey(Dat_Per, on_delete=models.CASCADE,verbose_name="es la fk de Datos de personas")

    def __str__(self):
        return f"{self.pk_int_pro}"
    
    class Meta:
        db_table = "Inf_Prof" 


    