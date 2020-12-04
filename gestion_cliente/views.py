from django.shortcuts import render , redirect  , get_object_or_404 
from django.views.generic.edit import CreateView, UpdateView, View , DeleteView
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView 
from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.urls import reverse_lazy
from .forms import ClienteForm , UserForm , UserModForm
from .models import Cliente




class CrearCliente(View):

    def get(self, request, *args, **kwargs):

        cli_form = ClienteForm()
        user_form = UserForm()
        return render(request, 'agregar_cliente.html', {
            'user_form': user_form,
            'cli_form':  cli_form
        })

    def post(self, request, *args, **kwargs):

        cli_form = ClienteForm(request.POST)
        user_form = UserForm(request.POST)

        if cli_form.is_valid() and user_form.is_valid():

            usuario = user_form.save(commit=False)
            usuario.set_password(user_form.cleaned_data['password1'])
            usuario.save()

            cliente = cli_form.save(commit=False)

            cliente.user = usuario

            cliente.save()

            obj, created = Group.objects.get_or_create(name='cliente')

            obj.user_set.add(cliente.user)

            messages.success(request, "Se a Guardado Correctamente")
            cli_form = ClienteForm()
            user_form = UserForm()
            return render(request, 'agregar_cliente.html', {
                'user_form': user_form,
                'cli_form':  cli_form
            })

        messages.error(request, "Hubo un error al querer crear un Cliente")

        return render(request, 'agregar_cliente.html', {
            'user_form': user_form,
            'cli_form':  cli_form
        })


class ListaCliente(ListView):

    model = Cliente
    template_name = 'listado_cliente.html'
    paginate_by = 100
  



def actualizar_cliente(request, pk):


    # pylint: disable=maybe-no-member
    cliente = get_object_or_404(Cliente,id=pk)
   
    # pylint: disable=maybe-no-member
    usuario = User.objects.get(id=cliente.user.id)

    user_form = UserModForm(instance=usuario)
    cli_form = ClienteForm(instance=cliente)
    

    if request.method == 'POST':

        cli_form = ClienteForm(request.POST, instance=cliente)
        user_form = UserModForm(request.POST, instance=usuario)

        if cli_form.is_valid() and user_form.is_valid():

            usuario = user_form.save()

            cliente = cli_form.save(commit=False)

            cliente.save()

            cli_form = ClienteForm(instance=cliente)
            user_form = UserModForm(instance=usuario)

    return render(request, 'modificar_cliente.html', {'cli_form': cli_form, 'user_form': user_form})




class  EliminarCliente(DeleteView):

    template_name  =  'eliminar_cliente.html'
    model  = Cliente
    success_url = reverse_lazy('lista_cliente')




class DetalleCliente(DetailView):

    
    template_name  =  'detalle_cliente.html'
    model  = Cliente
    success_url = reverse_lazy('lista_cliente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

   