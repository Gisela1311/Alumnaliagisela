
from django.shortcuts import render, redirect
#from .forms import InfProfForm
from .models import *

def pagina_inicio(request): 
    return render(request, 'app_alumnalia/inicio.html')
                  


# Vista para añadir un nuevo formador
def nuevo_formador(request):
    if request.method == "POST":
        form = InfProfForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_alumnalia:')
    else:
        form = Formadores()
    return render(request, 'alumnalia.es/nuevoformador.html', {'form': form})


# views.py
#from django.shortcuts import render, redirect
#from .forms import DatosPersonalesForm

def datos_personales_view(request):
    if request.method == 'POST':
        form = DatosPersonalesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirigir a una página de éxito
    else:
        form = DatosPersonalesForm()
    return render(request, 'datos_personales.html', {'form': form})
# views.py

def success_view(request):
    return render(request, 'success.html')

#form = InfProfForm():
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



