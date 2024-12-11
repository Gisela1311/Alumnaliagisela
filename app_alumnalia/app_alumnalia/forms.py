from django import forms
from .models import Dat_Per, Inf_Prof



class Dat_PerForm(forms.ModelForm):
    class Meta:
        model = Dat_Per
        fields = [
            'nom_per', 'dni_per', 'cn_per', 'tel_per', 'email_per', 
            'dir_per', 'sex_per', 'uso_datos_per', 'term_per', 'noti_per'
        ]

class Inf_ProfForm(forms.ModelForm):
    class Meta:
        model = Inf_Prof
        fields = [
            'tit_inf_pro', 'tit_esp_inf_pro', 'esp_inf_pro', 'exp_inf_pro',
            'for_imp_inf_pro', 'cv_adj_inf_pro', 'mod_inf_pro', 'tipo_alu_inf_pro',
            'tipo_alu_esp_inf_pro', 'franja_inf_pro', 'cert_inf_pro', 'cert_esp_inf_pro',
            'herr_inf_pro', 'herr_esp_inf_pro', 'comp_dig_inf_pro', 'comp_dig_esp_inf_pro', 'fk_per_inf_pro'
        ]

