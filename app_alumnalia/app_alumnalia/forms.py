from django import forms
from .models import Inf_Prof, Dat_Per


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
            'dir_per',
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
            'dir_per': 'Dirección',
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
            'cv_adj_inf_pro',
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
            'fk_per_inf_pro'
        ]
        labels = {
            'tit_inf_pro': 'Título académico más alto obtenido',
            'tit_esp_inf_pro': 'Especificar título',
            'esp_inf_pro': 'Área de especialización principal',
            'exp_inf_pro': 'Años de experiencia como formador/a',
            'for_imp_inf_pro': 'Tipo de formación impartida',
            'cv_adj_inf_pro': 'Adjunta tu currículum en formato PDF',
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
            'fk_per_inf_pro': 'Datos de personas'
        }
        widgets = {
            'tit_inf_pro': forms.Select(),
            'cv_adj_inf_pro': forms.FileInput(attrs={'accept': '.pdf'}),
        }

