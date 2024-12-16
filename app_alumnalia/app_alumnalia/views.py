
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic import FormView, TemplateView


                  
class InicioView(TemplateView):
    template_name = "alumnalia/inicio.html"
    context_object_name = ""



class datos_personales_view(TemplateView):
    template_name = "alumnalia/datospersonalesform.html"
    
    def get(self, request, *args, **kwargs): 
        form = DatPerForm() 
        return self.render_to_response({'form': form}) 
    
    def post(self, request, *args, **kwargs): 
        form = DatPerForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('inicio') # Redirigir después de guardar 
        return self.render_to_response({'form': form})
    
    
class datos_formador_view(TemplateView):
    template_name = "alumnalia/formadoresform.html"
    
    def get(self, request, *args, **kwargs): 
        form = FormadoresForm() 
        return self.render_to_response({'form': form}) 
    
    def post(self, request, *args, **kwargs): 
        form = FormadoresForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('alumnalia:inicio') # Redirigir después de guardar 
        return self.render_to_response({'form': form})

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








