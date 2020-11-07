from django.shortcuts import render , redirect
from django.views.generic.edit import CreateView , UpdateView , View
from django.views.generic.list import ListView
from django.contrib import messages
from .models import Cliente , Funcionario
from .forms import UserForm , ClienteForm , FuncionarioForm
from django.contrib.auth.models import Group , User


def home(request):
    
    return render(request, 'index.html', {})


class CrearFuncionario(View):
    
        

        def get(self, request, *args, **kwargs):
            
            
            func_form =  FuncionarioForm()
            user_form = UserForm()
            return render (request , 'agregarFuncionario.html', {
                'user_form' : user_form,
                'func_form' :  func_form
            } )

        def post(self, request, *args, **kwargs):

            func_form = FuncionarioForm(request.POST)
            user_form = UserForm(request.POST)
            
            if func_form.is_valid() and user_form.is_valid():
                
                usuario = user_form.save()
            
               

                funcionario = func_form.save(commit=False)

               

                funcionario.user = usuario

                funcionario.save()

                obj, created =  Group.objects.get_or_create(name='Funcionario')


                obj.user_set.add(funcionario.user)

                
                
                messages.success(request,"Se a Guardado Correctamente")
                func_form =  FuncionarioForm()
                user_form = UserForm()
                return render (request , 'agregarFuncionario.html', {
                    'user_form' : user_form,
                    'func_form' :  func_form
                } )

                

            messages.error(request,"Hubo un error al querer crear un Cliente")

            return render (request , 'agregarFuncionario.html', {
                    'user_form' : user_form,
                    'func_form' :  func_form
                } )



class ListaFuncionario(ListView):

    model = Funcionario
    template_name = 'funcionario_list.html'
    paginate_by = 100 


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




def ActulizarFuncionario(request , pk): 
    
    # pylint: disable=maybe-no-member
    funcionario = Funcionario.objects.get(id=pk)
    usuario = User.objects.get(id=funcionario.user.pk)
    
    func_form =  FuncionarioForm(instance=funcionario)
    user_form =  UserForm(instance=usuario)

    if request.method == 'POST':

       
        func_form = FuncionarioForm(request.POST , instance=funcionario )
        user_form =  UserForm(request.POST ,instance=usuario)

        if func_form.is_valid() and user_form.is_valid() :
            
            usuario  = user_form.save()
            
            funcionario = func_form.save(commit=False)
        
            funcionario.save()

            func_form = FuncionarioForm(instance=funcionario)
            user_form =  UserForm(instance=usuario)

    return render(request , 'actualizar_funcionario.html',{'func_form':func_form,'user_form':user_form})