from django.shortcuts import render, redirect
from .forms import Formadores

def nuevo_formador(request):
    if request.method == "POST":
        form = Formadores(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = Formadores()
    return render(request, 'alumnalia.es/nuevoformador.html', {'form': form})


# views.py
from django.shortcuts import render, redirect
from .forms import DatosPersonalesForm

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
