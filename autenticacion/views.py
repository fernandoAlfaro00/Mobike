from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login as do_login
from django.contrib.auth.models import User , Group
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from gestion_usuario.models import Cliente
from gestion_usuario.forms import ClienteForm 
from .forms import PUserForm


def home(request):

    
    return render(request, 'home.html')

def ingresar_datos(request):
    
    cli_form  =  ClienteForm()

    if request.method == 'POST':

        cli_form  = ClienteForm(request.POST)

        if cli_form.is_valid():
            cli_form.save()
            return redirect('home')

    return render(request, 'ingresarDatos.html',{'cli_form': cli_form})

def signup(request):

    form = PUserForm()
    if request.method == 'POST':

        form = PUserForm(request.POST)
        
        if form.is_valid():

            user = form.save()

            group ,created  =  Group.objects.get_or_create(name='PUsuario')

            group.user_set.add(user)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']


            user = authenticate(username=username, password=password)

        
            do_login(request, user)

            return redirect('ingresar_datos')
         
        return render (request, 'registration/signup.html',{'form':form})
  

    return render (request, 'registration/signup.html',{'form':form})


@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'