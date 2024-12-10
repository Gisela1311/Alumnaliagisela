from django import forms
from .models import Inf_Prof



class DatosPersonalesForm(forms.ModelForm):
    class Meta:
        model = DatosPersonales
        fields = '__all__'
        model = Inf_Prof
        fields = [
            'pk_inf_pro', 'tit_inf_pro', 'tit_esp_inf_pro', 'esp_inf_pro', 
            'exp_inf_pro', 'for_imp_inf_pro', 'cv_adj_inf_pro', 'mod_inf_pro', 
            'tipo_alu_inf_pro', 'tipo_alu_esp_inf_pro', 'franja_inf_pro', 
            'cert_inf_pro', 'cert_esp_inf_pro', 'herr_inf_pro', 'herr_esp_inf_pro', 
            'comp_dig_inf_pro', 'comp_dig_esp_inf_pro', 'fk_per_inf_pro'
        ]
