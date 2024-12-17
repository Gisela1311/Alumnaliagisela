from django.core.exceptions import ValidationError
from django.db import models
from .modelos.modelAdmin import Tipo_Usuario
from .modelos.modelDir import Comarca, Provincias, Comarca_provincias, Municipios

# controles de los campos
def validar_dni(value): 
    if not value.isalnum() or len(value) != 9: 
        raise ValidationError("El DNI debe tener 9 caracteres alfanuméricos.") # Tambien puede controla NIF, NIE Nacionalida española

def validar_longitud_nueve(value): 
    if len(str(value)) != 9: 
        raise ValidationError('El número debe tener exactamente 9 dígitos.')

# Tabla de Datos Personales

class Dat_Per(models.Model):
    pk_per = models.SmallAutoField(verbose_name="id de la Dat_Per", primary_key=True) 
    nom_per = models.CharField(max_length=150, verbose_name="Nombre de la Persona", null=False)    
    dni_per = models.CharField(max_length=15, unique=True, verbose_name="Nombre de la autoridad", validators=[validar_dni], null=False)
    fn_per = models.CharField(max_length=10,verbose_name="fecha de nacimiento de la persona", null=True)
    cn_per = models.CharField(max_length=150, verbose_name="Naciuonalidad de la persona", null=False)    
    tel_per = models.IntegerField(verbose_name="Teléfono de la persona", validators=[validar_longitud_nueve], null=True)
    email_per = models.EmailField(verbose_name="email de la persona")
    dir_per = models.CharField(max_length=150, verbose_name="Dirección de la persona", null=False) #models.ForeignKey(  on_delete=models.CASCADE, verbose_name="Dirección de la persona", default=0) #Direcciones
    
    genero=[
        ('', 'Seleccione una opción'),
        (1, 'Mujer'),
        (2, 'Hombre'),
        (3, 'Prefiero no específicar'),
        (4,'Otro')
    ]
    sex_per = models.IntegerField(
        verbose_name="Género de la persona",
        choices=genero,
        default=''
        )
       
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

    # INFORMACIÓN PROFESIONAL
    Titulo = [ 
        ('', 'Seleccione una opción'),
        (1, 'Técnico/a'), 
        (2, 'Grado universitario'), 
        (3, 'Máster'), 
        (4, 'Doctorado'),  
        (5, 'Otros'), 
        ]    
    #Otro (especificar)
    tit_inf_pro = models.IntegerField(
        verbose_name="Título académico más alto obtenido",
        choices=Titulo, 
        default=''
        )  
    tit_esp_inf_pro = models.CharField(max_length=30, verbose_name="Especifique tit_inf_pro")

    esp_inf_pro = models.CharField(max_length=15,verbose_name="¿En qué área está tu especialización principal?")  

    Experiencia = [ 
            ('', 'Seleccione una opción'),
            (1, 'Menos de 1 año'), 
            (2, 'De 1 a 3 años'), 
            (3, 'De 4 a 6 años'), 
            (4, 'Más de 6 años'),  
            ]   
    exp_inf_pro = models.IntegerField(
        verbose_name="¿Cuántos años de experiencia tienes como formador/a?",
        choices=Experiencia,
        default=''
        )  

    Formacion = [
        ('', 'Seleccione una opción'),
        (1, 'Formación profesional'),
        (2, 'Formación universitaria'),
        (3, 'Formación empresarial'),
        (4, 'Cursos en línea'),
        (5, 'Otros')
    ]
    for_imp_inf_pro = models.IntegerField(
        verbose_name="Qué tipo de formación has impartido",
        choices=Formacion,
        default=''
        )
    
    for_imp_esp_inf_pro = models.CharField(  max_length=255, verbose_name="Especifique que for_imp_inf_pro ha impartido")
    
    #cv_adj_inf_pro = models.CharField(max_length=15,verbose_name="Adjunta tu currículum en formato PDF.")  
    cv_adj_inf_pro = models.FileField(upload_to='pdfs/',verbose_name="Adjunta tu currículum en formato PDF.")
    
    # COMPETENCIAS Y CERTIFICACIONES
    opcion = [
        ('', 'Seleccione una opción'),
        (1, 'Sí'),
        (2, 'No'),
        (3, 'Especificar')
    ]
    cert_inf_pro = models.IntegerField(
        verbose_name="¿Tienes alguna certificación docente?",
        choices=opcion,
        default = '')  
    cert_esp_inf_pro = models.CharField(max_length=30, verbose_name="Especifique su cert_inf_pro")  
    #1,2,3,4,5 o 1,2,3,4 o 1,4,5
    herramientas = [
        ('', 'Seleccione una opción'),
        (1, 'Moodle'),
        (2, 'Microsoft Teams'),
        (3, 'Zoom'),
        (4, 'Google Classroom'),
        (5, 'Otros')
    ]
    herr_inf_pro = models.IntegerField(
        verbose_name="¿Qué herramientas tecnológicas utilizas en tus clases?",
        choices=herramientas, 
        default= '')  
    herr_esp_inf_pro = models.CharField(max_length=15, verbose_name="Especifique otra herr_inf_pro")

    comp_dig_inf_pro = models.IntegerField(
        verbose_name="¿Posees competencias digitales específicas (ej. DigCompEdu)?",
        choices=opcion,
        default= "")  
    
    comp_dig_esp_inf_pro = models.CharField(max_length=15, verbose_name="Especifique cuales")

    # PREFERENCIAS DE FORMACIÓN
    modalidad = [
        ('', 'Seleccione una opción'),
        (1, 'Presencial'),
        (2, 'En línea'),
        (3, 'Mixta')
    ]
    mod_inf_pro = models.IntegerField(
        verbose_name="Qué modalidades de enseñanza prefieres impartir",
        choices= modalidad,
        default= '1')
    
    alumno= [
        ('', 'Seleccione una opción'),
        (1, 'Jóvenes'),
        (2, 'Adultos'),
        (3, 'Empresas'),
        (4, 'Otros')
    ]  
    tipo_alu_inf_pro = models.IntegerField(
        verbose_name="Qué tipo de alumnado prefieres formar",
        choices=alumno,
        default='')  
    
    tipo_alu_esp_inf_pro = models.CharField(max_length=15, verbose_name="Especifique tipo_alu_inf_pro")  
    
    franja = [
        ('', 'Seleccione una opción'),
        (1, 'Mañana (8:00-14:00)'),
        (2, 'Tarde (14:00-20:00)'),
        (3, 'Noche (20:00-23:00)')
    ]
    franja_inf_pro = models.IntegerField(
        verbose_name="En qué franjas horarias estás disponible para impartir clases?",
        choices= franja, 
        default=''
        )  

    fk_per_inf_pro =  models.ForeignKey(Dat_Per, on_delete=models.CASCADE,verbose_name="es la fk de Datos de personas")

    def __str__(self):
        return f"{self.pk_inf_pro}"
    
    class Meta:
        db_table = "Inf_Prof" 




## tablas para el estudiante al ver una oferta

class OfertaEstudio(models.Model):
    TITULOS_CHOICES = [
        ('BACH', 'Bachillerato'),
        ('LIC', 'Licenciatura'),
        ('MAST', 'Máster'),
        ('DOC', 'Doctorado'),
    ]

    MODALIDADES_CHOICES = [
        ('PRESENCIAL', 'Presencial'),
        ('ONLINE', 'Online'),
        ('MIXTO', 'Mixto'),
    ]

    nom_Ofe_est = models.CharField(max_length=200)  # Nombre del curso/programa
    inst_Ofe_est = models.CharField(max_length=200)  # Nombre de la institución
    niv_Ofe_est = models.CharField(max_length=5, choices=TITULOS_CHOICES)  # Nivel de estudio
    mod_Ofe_est = models.CharField(max_length=10, choices=MODALIDADES_CHOICES)  # Modalidad de estudio
    dur_Ofe_est = models.IntegerField(help_text='Duración en meses')  # Duración del programa
    desc_Ofe_est = models.TextField(blank=True, null=True)  # Descripción del curso/programa
    fecha_inicio = models.DateField()  # Fecha de inicio
    fecha_fin = models.DateField()  # Fecha de finalización
    url_Ofe_est = models.URLField(blank=True, null=True)  # Enlace para más información
    def __str__(self):
        return f"{self.nom_Ofe_est} en {self.inst_Ofe_est}"


######### Area de Vistas de las Drecciones ##################
"""
class Domicilio(models.Model): #Domicilio o direccion donde vive
    class Meta: managed = False # No crear esta tabla en la base de datos 
    db_table = 'Domicilio'  #view_consultar_recetas
    pk_dom = models.AutoField(primary_key=True) 
    Domicilio = models.CharField(max_length=40) 
    tiempo = models.IntegerField(default=0) 
    dificultad = models.CharField(max_length=10) 
    categoria = models.CharField(max_length=10)  
    def __str__(self):
        return f"{self.pk_dom}"
    class Meta:
        db_table = "Domicilio" 
 
    pk_com, nom_com, pk_pro, nom_pro, pk_cam_pro, nom_cam_pro
"""

