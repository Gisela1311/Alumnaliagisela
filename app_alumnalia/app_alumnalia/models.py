from django.core.exceptions import ValidationError
from django.db import models
from .encryption_utils import encrypt_data, decrypt_data
from datetime import datetime, date
from .modelos.modelAdmin import Tipo_Usuario

from .modelos.modelDir import Comarca, Provincias, Comarca_provincias, Municipios, TipoVia


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
    fk_via = models.ForeignKey(TipoVia, on_delete=models.CASCADE, verbose_name="Tipo de via", null=True)
    dir_per = models.CharField(max_length=150, verbose_name="Dirección", null=False) #models.ForeignKey(  on_delete=models.CASCADE, verbose_name="Dirección de la persona", default=0) #Direcciones
    fk_pro = models.ForeignKey(Provincias, on_delete=models.CASCADE, verbose_name="Provincia", null=True) 
    fk_mun = models.ForeignKey(Municipios, on_delete=models.CASCADE, verbose_name="Municipio", null=True)
    
    #multiple choice para el género
    genero=[
        ('', 'Seleccione una opción'),
        ('1', 'Mujer'),
        ('2', 'Hombre'),
        ('3', 'Prefiero no especificar'),
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
    
    username = models.CharField(max_length=20, verbose_name="Usuario", unique=True, null=False)
    password = models.CharField(max_length=30, verbose_name="Contraseña", null=False)
    
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
        self.username = encrypt_data(self.username)
        self.password = encrypt_data(self.password)
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
    
    def get_username(self): 
        return decrypt_data(self.username)
    
    def get_password(self): 
        return decrypt_data(self.password)
    
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
        ('1', 'Sin estudios'), 
        ('2', 'Primaria'),  
        ('3', 'Secundaria'),
        ('4', 'Bachillerato'), 
        ('5', 'Técnico/a'), 
        ('6', 'Grado universitario'),  
        ('7', 'Máster'), 
        ('8', 'Doctorado'),  
        ('9', 'Otros'),
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
    cv_adj_inf_pro = models.FileField(upload_to='pdfs/',verbose_name="Adjunta tu currículum en formato PDF.",null=True, blank=True)
    
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


class Info_Estu(models.Model):
    pk_inf_est = models.SmallAutoField(verbose_name="id de la Información Estudiante", primary_key=True) 
    int_form_inf_est= models.CharField(max_length=15,verbose_name="intereses formativos")
    que_que_est= models.CharField(max_length=15,verbose_name="qué querrían estudiar")
    que_has_est= models.CharField(max_length=15,verbose_name=" qué han estudiado")
    de_que_han_trab= models.CharField(max_length=15,verbose_name="de qué han trabajado")
    de_que_que_trab= models.CharField(max_length=15,verbose_name="de qué querrían trabajar")
    rang_sal_des= models.FloatField(max_length=2,verbose_name="rango salarial deseado")
    cv_adj_inf_est = models.FileField(upload_to='pdfs/',verbose_name="Adjunta tu currículum en formato PDF.",null=True, blank=True)
    fk_per_inf_est= models.ForeignKey(Dat_Per, on_delete=models.CASCADE,verbose_name="fk de Datos de personas")

    def __str__(self):
        return f"{self.pk_inf_est}"
    class Meta:
        db_table = "Info_Estu" 

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


