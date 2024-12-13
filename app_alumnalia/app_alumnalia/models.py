from django.core.exceptions import ValidationError
from django.db import models

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
        ('1', 'Mujer'),
        ('2', 'Hombre'),
        ('3', 'Prefiero no específicar'),
        ('4','Otro')
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
        ('1', 'Técnico/a'), 
        ('2', 'Grado universitario'), 
        ('3', 'Máster'), 
        ('4', 'Doctorado'),  
        ('5', 'Otros'), #Otro (especificar)
        ]    

    tit_inf_pro = models.IntegerField(
        verbose_name="Título académico más alto obtenido",
        choices=Titulo, 
        default=''
        )  
    tit_esp_inf_pro = models.CharField(max_length=30, verbose_name="Especifique tit_inf_pro")

    esp_inf_pro = models.CharField(max_length=15,verbose_name="¿En qué área está tu especialización principal?")  

    Experiencia = [ 
            ('', 'Seleccione una opción'),
            ('1', 'Menos de 1 año'), 
            ('2', 'De 1 a 3 años'), 
            ('3', 'De 4 a 6 años'), 
            ('4', 'Más de 6 años'),  
            ]   
    exp_inf_pro = models.IntegerField(
        verbose_name="¿Cuántos años de experiencia tienes como formador/a?",
        choices=Experiencia,
        default=''
        )  

    Formacion = [
        ('', 'Seleccione una opción'),
        ('1', 'Formación profesional'),
        ('2', 'Formación universitaria'),
        ('3', 'Formación empresarial'),
        ('4', 'Cursos en línea'),
        ('5', 'Otros')
    ]
    for_imp_inf_pro = models.IntegerField(
        verbose_name="Qué tipo de formación has impartido",
        choices=Formacion,
        default='')  
    
    for_imp_esp_inf_pro = models.CharField(  max_length=255, verbose_name="Especifique que for_imp_inf_pro ha impartido")
    
    #cv_adj_inf_pro = models.CharField(max_length=15,verbose_name="Adjunta tu currículum en formato PDF.")  
    cv_adj_inf_pro = models.FileField(upload_to='pdfs/',verbose_name="Adjunta tu currículum en formato PDF.")
    
    # COMPETENCIAS Y CERTIFICACIONES
    opcion = [
        ('', 'Seleccione una opción'),
        ('1', 'Sí'),
        ('2', 'No'),
        ('3', 'Especificar')
    ]
    cert_inf_pro = models.IntegerField(
        verbose_name="¿Tienes alguna certificación docente?",
        choices=opcion,
        default = '')  
    cert_esp_inf_pro = models.CharField(max_length=30, verbose_name="Especifique su cert_inf_pro")  

    herramientas = [
        ('', 'Seleccione una opción'),
        ('1', 'Moodle'),
        ('2', 'Microsoft Teams'),
        ('3', 'Zoom'),
        ('4', 'Google Classroom'),
        ('5', 'Otros')
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
        ('1', 'Presencial'),
        ('2', 'En línea'),
        ('3', 'Mixta')
    ]
    mod_inf_pro = models.IntegerField(
        verbose_name="Qué modalidades de enseñanza prefieres impartir",
        choices= modalidad,
        default= '1')
    
    alumno= [
        ('', 'Seleccione una opción'),
        ('1', 'Jóvenes'),
        ('2', 'Adultos'),
        ('3', 'Empresas'),
        ('4', 'Otros')
    ]  
    tipo_alu_inf_pro = models.IntegerField(
        verbose_name="Qué tipo de alumnado prefieres formar",
        choices=alumno,
        default='')  
    
    tipo_alu_esp_inf_pro = models.CharField(max_length=15, verbose_name="Especifique tipo_alu_inf_pro")  
    
    franja = [
        ('', 'Seleccione una opción'),
        ('1', 'Mañana (8:00-14:00)'),
        ('2', 'Tarde (14:00-20:00)'),
        ('3', 'Noche (20:00-23:00)')
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
    nom_cam_pro =  models.CharField(max_length=30, verbose_name="nombre de la Comarca_provincias")
    def __str__(self):
        return f"{self.pk_pro}"
    class Meta:
        db_table = "Comarca_provincias" 


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
######## familia porfesional ######
class Familia_Profesion(models.Model):
    pk_fm_pro= models.CharField(max_length=20,verbose_name="id de Entidad Formadora",primary_key=True)
    desc_fm_pro= models.CharField(max_length=200, verbose_name="Descripcion de la Familia Profesional")
    def __str__(self):
        return f"{self.pk_fm_pro}"
    class Meta:
        db_table = "Familia_Profesional" 


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
    area_prof_ent_for= models.CharField(max_length=44,verbose_name="Area Pofesional de Entidad Formadora")
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