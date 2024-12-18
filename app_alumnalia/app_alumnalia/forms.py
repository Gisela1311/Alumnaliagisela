from django import forms
from .models import Inf_Prof, Dat_Per, Info_Estu

class DatPerForm(forms.ModelForm):
    class Meta:
        model = Dat_Per
        fields = [
            'nom_per',
            'dni_per',
            'fn_per',
            'cn_per',
            'tel_per',
            'email_per',
            'fk_nom_via', 
            'dir_per',
            'fk_nom_pro',  
            'fk_nom_mun',  
            'sex_per',
            'uso_datos_per',
            'term_per',
            'noti_per'
        ]
        labels = {
            'nom_per': 'Nombre de la Persona',
            'dni_per': 'DNI',
            'fn_per': 'Fecha de Nacimiento',
            'cn_per': 'Nacionalidad',
            'tel_per': 'Teléfono',
            'email_per': 'Correo Electrónico',
            'fk_nom_via': 'Tipo de Vía', 
            'dir_per': 'Dirección',
            'fk_nom_pro': 'Provincia',  
            'fk_nom_mun': 'Municipio',  
            'sex_per': 'Género',
            'uso_datos_per': 'Consentimiento para Uso de Datos',
            'term_per': 'Aceptación de Términos y Condiciones',
            'noti_per': 'Desea Recibir Notificaciones'
        }
        widgets = {
            'fn_per': forms.DateInput(attrs={'type': 'date'}),
            'uso_datos_per': forms.CheckboxInput(),
            'term_per': forms.CheckboxInput(),
            'noti_per': forms.CheckboxInput(),
            'fk_nom_pro': forms.Select(),
            'fk_nom_mun': forms.Select(),
            'fk_nom_via': forms.Select()
        }

class FormadoresForm(forms.ModelForm):
    class Meta:
        model = Inf_Prof
        fields = [
            'tit_inf_pro',
            'tit_esp_inf_pro',
            'esp_inf_pro',
            'exp_inf_pro',
            'for_imp_inf_pro',
            'for_imp_esp_inf_pro',
            'mod_inf_pro',
            'tipo_alu_inf_pro',
            'tipo_alu_esp_inf_pro',
            'franja_inf_pro',
            'cert_inf_pro',
            'cert_esp_inf_pro',
            'herr_inf_pro',
            'herr_esp_inf_pro',
            'comp_dig_inf_pro',
            'comp_dig_esp_inf_pro',
            'fk_per_inf_pro',
            'cv_adj_inf_pro'
        ]
        labels = {
            'tit_inf_pro': 'Título académico más alto obtenido',
            'tit_esp_inf_pro': 'Especificar título',
            'esp_inf_pro': 'Área de especialización principal',
            'exp_inf_pro': 'Años de experiencia como formador/a',
            'for_imp_inf_pro': 'Tipo de formación impartida',
            'for_imp_esp_inf_pro':'especificar el tipo de formación impartida',
            'mod_inf_pro': 'Modalidades de enseñanza preferidas',
            'tipo_alu_inf_pro': 'Tipo de alumnado preferido',
            'tipo_alu_esp_inf_pro': 'Especificar tipo de alumnado',
            'franja_inf_pro': 'Franjas horarias disponibles',
            'cert_inf_pro': 'Certificación docente',
            'cert_esp_inf_pro': 'Especificar certificación',
            'herr_inf_pro': 'Herramientas tecnológicas utilizadas',
            'herr_esp_inf_pro': 'Especificar herramientas',
            'comp_dig_inf_pro': 'Competencias digitales específicas (ej. DigCompEdu)',
            'comp_dig_esp_inf_pro': 'Especificar competencias digitales',
            'fk_per_inf_pro': 'Datos de personas',
            'cv_adj_inf_pro': 'Adjunta tu currículum en formato PDF'
        }
        widgets = {
            # 'tit_inf_pro': forms.Select(),
            'cv_adj_inf_pro': forms.FileInput(attrs={'accept': '.pdf'}),
        }



class InfoEstuForm(forms.ModelForm):
    class Meta:
        model = Info_Estu
        fields = [
            'int_form_inf_est',
            'que_que_est',
            'que_has_est',
            'de_que_han_trab',
            'de_que_que_trab',
            'rang_sal_des',
            'cv_adj_inf_est',
            'fk_per_inf_est'
        ]
        labels = {
            'int_form_inf_est': 'Intereses Formativos',
            'que_que_est': 'Qué Querrían Estudiar',
            'que_has_est': 'Qué Han Estudiado',
            'de_que_han_trab': 'De Qué Han Trabajado',
            'de_que_que_trab': 'De Qué Querrían Trabajar',
            'rang_sal_des': 'Rango Salarial Deseado',
            'cv_adj_inf_est': 'Adjunta tu Currículum en Formato PDF',
            'fk_per_inf_est': 'Datos de Personas'
        }
        widgets = {
           
            'rang_sal_des': forms.NumberInput(),
            'cv_adj_inf_est': forms.FileInput(attrs={'accept': '.pdf'}),
        }
