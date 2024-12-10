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
