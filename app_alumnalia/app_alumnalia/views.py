
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic import FormView, TemplateView


                  
class InicioView(TemplateView):
    template_name = "alumnalia/inicio.html"
    context_object_name = ""


class datos_formardor_view(TemplateView):
    template_name = "alumnalia/formadoresform.html"
    context_object_name = ""


class datos_personales_view(TemplateView):
    template_name = "alumnalia/datospersonalesform.html"
    context_object_name = ""


# class success_view(TemplateView):
#     return render(request, 'success.html')

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



