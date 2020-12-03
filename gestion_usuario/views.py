from django.utils.crypto import get_random_string
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect , get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, View
from django.views.generic.list import ListView
from django.contrib import messages
from .models import  Funcionario
from .forms import UserForm,  FuncionarioForm
from django.contrib.auth.models import Group, User


def home(request):

    return render(request, 'user_base.html', {})





class CrearFuncionario(View):

    def get(self, request, *args, **kwargs):

        per_form = ClienteForm()
        user_form = UserForm()
        return render(request, 'AgregarUsuario.html', {
            'user_form': user_form,
            'per_form':  per_form
        })

    def post(self, request, *args, **kwargs):

        per_form = ClienteForm(request.POST)
        user_form = UserForm(request.POST)

        if per_form.is_valid() and user_form.is_valid():

            usuario = user_form.save(commit=False)
            usuario.set_password(user_form.cleaned_data['password1'])
            usuario.save()

            funcionario = per_form.save(commit=False)

            funcionario.user = usuario

            funcionario.save()

            obj, created = Group.objects.get_or_create(name='Funcionario')

            obj.user_set.add(funcionario.user)

            messages.success(request, "Se a Guardado Correctamente")
            per_form = ClienteForm()
            user_form = UserForm()
            return render(request, 'AgregarUsuario.html', {
                'user_form': user_form,
                'per_form':  per_form
            })

        messages.error(request, "Hubo un error al querer crear un Cliente")

        return render(request, 'AgregarUsuario.html', {
            'user_form': user_form,
            'per_form':  per_form
        })


class ListaFuncionario(ListView):

    model = User
    template_name = 'ListadoUsuario.html'
    paginate_by = 100
    queryset = User.objects.filter(is_superuser=False)
 

# class ActulizarFuncionario(UpdateView):

#     model = Funcionario

#     template_name = 'actualizar_funcionario.html'
#     form_class  = FuncionarioForm
#     second_form_class = UserForm


#     def get_context_data(self, **kwargs):
#         context = super(ActulizarFuncionario, self).get_context_data(**kwargs)


#         func = self.object
#         user = User.objects.get(id=func.user.id)
#         context['form_user'] =  self.second_form_class(instance=user)
#         return context

#     def get_absolute_url(self):
#         return redirect('home')


def actualizar_usuario(request, pk):

    # pylint: disable=maybe-no-member
    
    usuario = get_object_or_404(User,id=pk)
    user_form = UserForm(instance=usuario)
    try:
        cliente = Cliente.objects.get(user_id=usuario.id)
        per_form = ClienteForm(instance=cliente)
    except ObjectDoesNotExist:
        return render(request, 'ModificarUsuario.html', {'per_form': per_form, 'user_form': user_form})

    try:
        cliente = Funcionario.objects.get(user_id=usuario.id)
        per_form = FuncionarioForm(instance=Funcionario)
    except ObjectDoesNotExist:
        return render(request, 'ModificarUsuario.html', {'per_form': per_form, 'user_form': user_form})     

        
        
       
    
    
 

    if request.method == 'POST':

        per_form = FuncionarioForm(request.POST, instance=funcionario)
        user_form = UserForm(request.POST, instance=usuario)

        if per_form.is_valid() and user_form.is_valid():

            usuario = user_form.save()

            funcionario = per_form.save(commit=False)

            funcionario.save()

            per_form = FuncionarioForm(instance=funcionario)
            user_form = UserForm(instance=usuario)

    return render(request, 'ModificarUsuario.html', {'per_form': per_form, 'user_form': user_form})
