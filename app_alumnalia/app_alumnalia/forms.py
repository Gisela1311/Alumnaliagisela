from django.forms import ModelForm
from .models import *

class Formadores(ModelForm):
    class Meta:
        model = 
        fields = ['titulo', 'especializacion', 'experiencia', 'formacion', 'cv', 'modalidad', 'tipo_alumno', 'franja', 'certificacion', 'herramientas', 'competencias']


# forms.py

class DatosPersonalesForm(forms.ModelForm):
    class Meta:
        model = DatosPersonales
        fields = '__all__'
