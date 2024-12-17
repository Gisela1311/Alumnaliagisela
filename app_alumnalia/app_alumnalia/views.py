import base64
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.views.generic import FormView, TemplateView, View
from django.shortcuts import render, get_object_or_404, redirect 


                  
class InicioView(TemplateView):
    template_name = "app_alumnalia/inicio.html"
    context_object_name = ""

class PerfilusuarioView(TemplateView):
    template_name = "app_alumnalia/perfilusuario.html"
    context_object_name = ""

class oferta_personalizada(TemplateView):
    template_name= "app_alumnalia/ofertassugeridas.html"
    context_object_name = ""

class datos_personales_estudiantes_view(View):
    template_name = "app_alumnalia/datospersonalesestudiantesform.html"
    
    def get(self, request): 
        form = DatPerForm() 
        return render(request, self.template_name, {'form': form}) 
    
    def post(self, request): 
        form = DatPerForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('oferta_personalizada') # Modificar al formulario datos estudiante cuando este el modelo hecho
        return render(request, self.template_name, {'form': form})
    
class datos_personales_formadores_view(View):
    template_name = "app_alumnalia/datospersonalesformadoresform.html"
    
    def get(self, request): 
        form = DatPerForm() 
        return render(request, self.template_name, {'form': form}) 
    
    def post(self, request): 
        form = DatPerForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('datos_formador')
        return render(request, self.template_name, {'form': form})    
    
class datos_formador_view(FormView):
    template_name = "app_alumnalia/formadoresform.html"
    
    def get(self, request, *args, **kwargs): 
        form = FormadoresForm() 
        return self.render_to_response({'form': form}) 
      
    def post(self, request, *args, **kwargs): 
        form = FormadoresForm(request.POST, request.FILES)  # Asegúrate de incluir request.FILES
        if form.is_valid(): 
            form.save() 
            return redirect('oferta_personalizada')  # Redirigir después de guardar 
        return self.render_to_response({'form': form})




# Archivo
#cod_Arc,tipo_arc,B64_arc
#1,pdf,Base64:Pdf
#2,img,Base64:img


# class success_view(TemplateView):
#     return render(request, 'success.html')


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


# Metodos de actualizacion de datos
# Eliminar
"""
def eliminar_fila(request, id): 
    fila = get_object_or_404(Dat_Per, id = id) 
    if request.method == 'POST': 
        fila.delete() 
        return redirect('lista_filas') # Redirige a una página de lista de filas o donde desees 
    return render(request, 'confirmar_eliminacion.html', {'fila': fila})

def lista_filas(request): 
    filas = Dat_Per.objects.all() 
    return render(request, 'lista_filas.html', {'filas': filas})
"""
"""
def eliminar_documento(request, id): 
    documento = get_object_or_404(Dat_Per, id=id) 
    if request.method == 'POST': 
        documento.delete() 
        return redirect('lista_documentos') # Redirige a una página de lista de documentos o donde desees 
    return render(request, 'confirmar_eliminacion.html', {'documento': documento})
def lista_documentos(request): 
    documentos = Dat_Per.objects.all() 
    return render(request, 'lista_documentos.html', {'documentos': documentos})
"""


