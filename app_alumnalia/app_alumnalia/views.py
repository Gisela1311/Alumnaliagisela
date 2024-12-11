
from django.shortcuts import render, redirect
#from .forms import InfProfForm
from .forms import Dat_PerForm, Inf_ProfForm
from .models import *


def pagina_inicio(request): 
    return render(request, 'app_alumnalia/inicio.html')
                  

# Vista para añadir un nuevo formador
def nuevo_formador(request):
    if request.method == "POST":
        form = Inf_ProfForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_alumnalia:')
    else:
        form = Inf_ProfForm()
    return render(request, 'alumnalia.es/nuevoformador.html', {'form': form})


# views.py
#from django.shortcuts import render, redirect
#from .forms import DatosPersonalesForm

def dat_per_view(request):
    if request.method == 'POST':
        form = Dat_PerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success') #Redirigir a una página de éxito
    else:
        form = Dat_PerForm()
    return render(request, 'dat_per_form.html', {'form': form})



#form = Inf_ProfForm():
#    return render(request, 'app_alumnalia/.html', {'form': form})

# def nuevo_estudiante(request):
#     if request.method == "POST":
#         form = InfProfForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('app_alumnalia:lista_inf_prof')
#     else:
#         form = InfProfForm()
#     return render(request, 'app_alumnalia/nuevo_inf_prof.html', {'form': form})








