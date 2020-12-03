from django.shortcuts import render , reverse , get_object_or_404
from django.urls import reverse_lazy 
from django.views.generic.detail  import DetailView 
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView , DeleteView  , FormView
from .models import Bicicleta
from django.forms import formset_factory  
from .forms import BicicletaForm

from django.contrib.auth.decorators import login_required

class CrearBicicleta(FormView):
    form_class = formset_factory(BicicletaForm)
    model = Bicicleta
    template_name =  'agregar_bicicleta.html'
   

    def get_success_url(self):
        return reverse('listado_bicicleta')

    def form_valid(self,form):

        for f in form:
            f.save()

        return super(CrearBicicleta, self).form_valid(form)


class ModificarBicicleta(UpdateView):
    model = Bicicleta
    
    fields = ['codigo', 'estacion' , 'estado']
    template_name =  'modificar_bicicleta.html'
    
    def get_success_url(self):
        return reverse('listado_bicicleta')


class ListaBicicleta(ListView):

    model = Bicicleta
    template_name = 'listado_bicicleta.html'
    paginate_by = 100
   


class EliminarBicicleta(DeleteView):
    model = Bicicleta
    success_url = reverse_lazy('listado_bicicleta')
    template_name=  'confirmar_eliminacion_bicicleta.html'

  
    

class DetalleBicicleta(DetailView):

    model = Bicicleta
    template_name = 'detalle_bicicleta.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context