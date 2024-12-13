
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.views.generic import FormView, TemplateView, View


                  
class InicioView(TemplateView):
    template_name = "app_alumnalia/inicio.html"
    context_object_name = ""



class datos_personales_view(View):
    template_name = "app_alumnalia/datospersonalesform.html"
    
    def get(self, request): 
        form = DatPerForm() 
        return render(request, self.template_name, {'form': form}) 
    
    def post(self, request): 
        form = DatPerForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('inicio') # Redirige a la vista de inicio u otra vista de tu elección 
        return render(request, self.template_name, {'form': form})
    
class datos_formador_view(FormView):
    template_name = "app_alumnalia/formadoresform.html"
    
    def get(self, request, *args, **kwargs): 
        form = FormadoresForm() 
        return self.render_to_response({'form': form}) 
    
    def post(self, request, *args, **kwargs): 
        form = FormadoresForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('app_alumnalia:inicio') # Redirigir después de guardar 
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








