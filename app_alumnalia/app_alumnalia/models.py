from django.core.exceptions import ValidationError
from django.db import models
from .encryption_utils import encrypt_data, decrypt_data
from datetime import datetime, date

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
    nom_per = models.CharField(max_length=150, verbose_name="Nombre", null=False)    
    dni_per = models.CharField(max_length=15, unique=True, verbose_name="DNI/NIE", validators=[validar_dni], null=False)
    fn_per = models.DateField(verbose_name="Fecha de nacimiento")
    fn_per_enc = models.CharField(max_length=15, verbose_name="Fecha de nacimiento encriptada", default="")
    cn_per = models.CharField(max_length=150, verbose_name="Nacionalidad", null=False)    
    tel_per = models.IntegerField(verbose_name="Teléfono", validators=[validar_longitud_nueve])
    tel_per_enc = models.CharField(max_length=10, verbose_name="Teléfono encriptada", default="")
    email_per = models.EmailField(verbose_name="Email")
    dir_per = models.CharField(max_length=150, verbose_name="Dirección", null=False) #models.ForeignKey(  on_delete=models.CASCADE, verbose_name="Dirección de la persona", default=0) #Direcciones
    
    genero=[
        ('', 'Seleccione una opción'),
        ('1', 'Mujer'),
        ('2', 'Hombre'),
        ('3', 'Prefiero no responder'),
        ('4','Otro')
    ]
    sex_per = models.CharField(
        verbose_name="Género de la persona",
        choices=genero,
        default='', 
        max_length=1
        )
       
    # Si se acepta o no la Declaraciones y Consentimientos de sus datos
    uso_datos_per = models.BooleanField(verbose_name="Fines de gestión académica y administrativa",default=False)
    term_per = models.BooleanField(verbose_name="Términos y condiciones",default=False)
    noti_per = models.BooleanField(verbose_name="Notificaciones de oportunidades formativas",default=False)
    
    # Sobrescribir el método save para encriptar datos antes de guardar 
    def save(self, *args, **kwargs): 
        
        self.nom_per = encrypt_data(self.nom_per) 
        self.dni_per = encrypt_data(self.dni_per)
        self.fn_per_enc = encrypt_data(self.fn_per.isoformat())
        self.cn_per = encrypt_data(self.cn_per) 
        self.tel_per_enc = encrypt_data(str(self.tel_per))
        self.email_per = encrypt_data(self.email_per) 
        self.dir_per = encrypt_data(self.dir_per)
        self.sex_per = encrypt_data(self.sex_per)
        self.fn_per = date(2001, 1, 1)
        self.tel_per = 666666666
        super(Dat_Per, self).save(*args, **kwargs) 
        
    # Método para desencriptar datos sensibles 
    def get_nom_per(self): 
        return decrypt_data(self.nom_per) 
    
    def get_dni_per(self): 
        return decrypt_data(self.dni_per)

    def get_fn_per(self): 
        return decrypt_data(self.fn_per_enc)
    
    def get_cn_per(self): 
        return decrypt_data(self.cn_per) 
    
    def get_tel_per(self): 
        return decrypt_data(self.tel_per_enc)
    
    def get_email_per(self): 
        return decrypt_data(self.email_per) 
    
    def get_dir_per(self): 
        return decrypt_data(self.dir_per)
    
    def get_sex_per(self): 
        return decrypt_data(self.sex_per)
    
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

    tit_inf_pro = models.CharField(
        verbose_name="Título académico más alto obtenido",
        choices=Titulo, 
        default='', max_length=1
        )  
    tit_esp_inf_pro = models.CharField(max_length=15, verbose_name="Especifique título")

    esp_inf_pro = models.CharField(max_length=15,verbose_name="¿En qué área está tu especialización principal?")  

    Experiencia = [ 
            ('', 'Seleccione una opción'),
            ('1', 'Menos de 1 año'), 
            ('2', 'De 1 a 3 años'), 
            ('3', 'De 4 a 6 años'), 
            ('4', 'Más de 6 años'),  
            ]   
    exp_inf_pro = models.CharField(
        verbose_name="¿Cuántos años de experiencia tienes como formador/a?",
        choices=Experiencia,
        default='', max_length=1
        )  

    Formacion = [
        ('', 'Seleccione una opción'),
        ('1', 'Formación profesional'),
        ('2', 'Formación universitaria'),
        ('3', 'Formación empresarial'),
        ('4', 'Cursos en línea'),
        ('5', 'Otros')
    ]
    for_imp_inf_pro = models.CharField(
        verbose_name="Qué tipo de formación has impartido",
        choices=Formacion,
        default='', max_length=1)  
    
    for_imp_esp_inf_pro = models.CharField(  max_length=255, verbose_name="Especifique que formación ha impartido")
    
    #cv_adj_inf_pro = models.CharField(max_length=15,verbose_name="Adjunta tu currículum en formato PDF.")  
    cv_adj_inf_pro = models.FileField(upload_to='pdfs/',verbose_name="Adjunta tu currículum en formato PDF.")
    
    # COMPETENCIAS Y CERTIFICACIONES
    opcion = [
        ('', 'Seleccione una opción'),
        ('1', 'Sí'),
        ('2', 'No')
    ]
    cert_inf_pro = models.CharField(
        verbose_name="¿Tienes alguna certificación docente?",
        choices=opcion,
        default = '', max_length=1)  
    cert_esp_inf_pro = models.CharField(max_length=15, verbose_name="Especifique su certificación")  

    herramientas = [
        ('', 'Seleccione una opción'),
        ('1', 'Moodle'),
        ('2', 'Microsoft Teams'),
        ('3', 'Zoom'),
        ('4', 'Google Classroom'),
        ('5', 'Otros')
    ]
    herr_inf_pro = models.CharField(
        verbose_name="¿Qué herramientas tecnológicas utilizas en tus clases?",
        choices=herramientas, 
        default= '', max_length=1)  
    herr_esp_inf_pro = models.CharField(max_length=15, verbose_name="Especifique otra herramienta tecnológica")

    comp_dig_inf_pro = models.CharField(
        verbose_name="¿Posees competencias digitales específicas (ej. DigCompEdu)?",
        choices=opcion,
        default= "", max_length=1) 
    
    comp_dig_esp_inf_pro = models.CharField(max_length=15, verbose_name="Especifique cuales")

    # PREFERENCIAS DE FORMACIÓN
    modalidad = [
        ('', 'Seleccione una opción'),
        ('1', 'Presencial'),
        ('2', 'En línea'),
        ('3', 'Mixta')
    ]
    mod_inf_pro = models.CharField(
        verbose_name="Qué modalidades de enseñanza prefieres impartir",
        choices= modalidad,
        default= '', max_length=1)
    
    alumno= [
        ('', 'Seleccione una opción'),
        ('1', 'Jóvenes'),
        ('2', 'Adultos'),
        ('3', 'Empresas'),
        ('4', 'Otros')
    ]  
    tipo_alu_inf_pro = models.CharField(
        verbose_name="Qué tipo de alumnado prefieres formar",
        choices=alumno,
        default='', max_length=1)  
    
    tipo_alu_esp_inf_pro = models.CharField(max_length=15, verbose_name="Especifique el tipo de alumnos")  
    
    franja = [
        ('', 'Seleccione una opción'),
        ('1', 'Mañana (8:00-14:00)'),
        ('2', 'Tarde (14:00-20:00)'),
        ('3', 'Noche (20:00-23:00)')
    ]
    franja_inf_pro = models.CharField(
        verbose_name="En qué franjas horarias estás disponible para impartir clases?",
        choices= franja, 
        default='', max_length=1
        )  

    fk_per_inf_pro =  models.ForeignKey(Dat_Per, on_delete=models.CASCADE,verbose_name="fk de Datos de personas")

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
    nom_com =  models.CharField(max_length=30, verbose_name="Nombre de la Comarca")
    def __str__(self):
        return f"{self.nom_com}"
    class Meta:
        db_table = "Comarca" 

#2 tabla de los Municipios
class Municipios(models.Model):
    pk_mun = models.SmallAutoField(
        verbose_name="id de Municipios", 
        primary_key=True
        ) 
    nom_mun =  models.CharField(max_length=30, verbose_name="Nombre del Municipio")
    fk_com = models.ForeignKey(Comarca, on_delete=models.CASCADE, related_name='Municipios')
    def __str__(self):
        return f"{self.nom_mun}"
    class Meta:
        db_table = "Municipios" 

#3 tabla de las Provincias
class Provincias(models.Model):
    pk_pro = models.SmallAutoField(
        verbose_name="id de Provincias", 
        primary_key=True
        ) 
    nom_pro =  models.CharField(max_length=30, verbose_name="Nombre de la Provincia")
    def __str__(self):
        return f"{self.pk_pro}"
    class Meta:
        db_table = "Provincias" 

#4 tabla relación Comarcas con Provincias
class Comarca_provincias(models.Model):
    pk_cam_pro = models.SmallAutoField(
        verbose_name="id de Comarca_provincias", 
        primary_key=True
        ) 
    fk_com = models.ForeignKey(Comarca, on_delete=models.CASCADE, related_name='Comarca_provincias', default=1)
    fk_pro = models.ForeignKey(Provincias, on_delete=models.CASCADE, related_name='Comarca_provincias', default=1)
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
        db_table = "Familia_Profecional" 


######## Entidad Formadora ###### tabla Origen de datos foap2024
##7 Entidad Formadora -> Ent_For 
class Ent_For(models.Model):
    pk_ent_for= models.CharField(max_length=20,verbose_name="id de Entidad Formadora",primary_key=True)
    nom_ent_for= models.CharField(max_length=44, verbose_name="Nombre")
    Area_for_ent_for= models.CharField(max_length=44,verbose_name="Area de formacion")
    email_ent_for= models.EmailField(verbose_name="Email")
    nif_ent_for= models.CharField(max_length=20,verbose_name="NIF")
    fec_fin_ent_for= models.DateField(verbose_name="Fecha de fin")
    fec_ini_ent_for= models.DateField(verbose_name="Fecha de inicio")
    area_prof_ent_for= models.CharField(max_length=44,verbose_name="Area Porfesional")
    cp_ent_for= models.CharField(max_length=5,verbose_name="Codigo postal", default="")
    web_ent_for =models.URLField (max_length=100,verbose_name="URL de la web") 
    horas_ent_for= models.IntegerField(verbose_name="Horas")
    idt_ent_for= models.IntegerField(verbose_name="Identificador")
    den_ent_for= models.CharField (max_length=100,verbose_name="Denominacion")
    amb_ent_for= models.CharField (max_length=100,verbose_name="Ambito")
    mod_ent_for= models.CharField (max_length=50,verbose_name="Modalidad")
    num_grupo= models.IntegerField(verbose_name="Numero de grupo")
    tel_ent_for= models.IntegerField (
        validators=[validar_longitud_nueve],
        verbose_name="Telefono", default=0
        )
    fk_mun_ent_for = models.ForeignKey(Municipios, on_delete=models.CASCADE, related_name='Municipios') #cod_municipo (nom_municipio,) ok
    fk_com_ent_for = models.ForeignKey(Comarca, on_delete=models.CASCADE, related_name='Comarca') #cd_comarca (nom_comarca) ok
    fk_fam_pro =models.ForeignKey(Familia_Profesion, on_delete=models.CASCADE, related_name='Familia_Profesion')

    def __str__(self):
        return f"{self.nom_ent_for}"
    class Meta:
        db_table = "Ent_For" 