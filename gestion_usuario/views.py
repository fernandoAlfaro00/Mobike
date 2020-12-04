from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, View, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import Group, User
from .models import Funcionario
from .forms import UserForm,  FuncionarioForm , UserModForm


def home(request):

    return render(request, 'user_base.html', {})


class CrearFuncionario(View):

    def get(self, request, *args, **kwargs):

        func_form = FuncionarioForm()
        user_form = UserForm()
        return render(request, 'agregar_funcionario.html', {
            'user_form': user_form,
            'func_form':  func_form
        })

    def post(self, request, *args, **kwargs):

        func_form = FuncionarioForm(request.POST)
        user_form = UserForm(request.POST)

        if func_form.is_valid() and user_form.is_valid():

            usuario = user_form.save(commit=False)
            usuario.set_password(user_form.cleaned_data['password1'])
            usuario.save()

            funcionario = func_form.save(commit=False)

            funcionario.user = usuario

            funcionario.save()

            obj, created = Group.objects.get_or_create(name='Funcionario')

            obj.user_set.add(funcionario.user)

            messages.success(request, "Se a Guardado Correctamente")
            func_form = FuncionarioForm()
            user_form = UserForm()
            return render(request, 'agregar_funcionario.html', {
                'user_form': user_form,
                'func_form':  func_form
            })

        messages.error(request, "Hubo un error al querer crear un Funcionario")

        return render(request, 'agregar_funcionario.html', {
            'user_form': user_form,
            'func_form':  func_form
        })


class ListaFuncionario(ListView):

    model = Funcionario
    template_name = 'lista_funcionario.html'
    paginate_by = 100



def actualizar_Funcionario(request, pk):

   
    funcionario = get_object_or_404(Funcionario, id=pk)

    # pylint: disable=maybe-no-member
    usuario = User.objects.get(id=funcionario.user.id)

    user_form = UserModForm(instance=usuario)
    func_form = FuncionarioForm(instance=funcionario)

    if request.method == 'POST':

        func_form = FuncionarioForm(request.POST, instance=funcionario)
        user_form = UserModForm(request.POST, instance=usuario)

        if func_form.is_valid() and user_form.is_valid():

            usuario = user_form.save()

            funcionario = func_form.save(commit=False)

            funcionario.save()

            func_form = FuncionarioForm(instance=funcionario)
            user_form = UserModForm(instance=usuario)

    return render(request, 'modifcar_funcionario.html', {'func_form': func_form, 'user_form': user_form})


class EliminarFuncionario(DeleteView):

    template_name = 'confirmar_eliminacion_funcionario.html'
    model = Funcionario
    success_url = reverse_lazy('lista_Funcionario')


class DetalleFuncionario(DetailView):

    template_name = 'detalle_funcionario.html'
    model = Funcionario
    success_url = reverse_lazy('lista_funcionario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
