from django.forms import ModelForm
from .models import *

class Formadores(ModelForm):
    class Meta:
        model = 
        fields = ['titulo', 'especializacion', 'experiencia', 'formacion', 'cv', 'modalidad', 'tipo_alumno', 'franja', 'certificacion', 'herramientas', 'competencias']

