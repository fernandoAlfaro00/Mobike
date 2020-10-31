from django import forms
from .models import Cliente , Funcionario
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class ClienteForm(forms.ModelForm):
    """
    docstring
    """
    class Meta:
        
        model = Cliente
        
        fields = '__all__'
        exclude  = ['user']

class FuncionarioForm(forms.ModelForm):
    """
    docstring
    """
    class Meta:
        
        model = Funcionario
        
        fields = '__all__'
        exclude  = ['user']


class UserForm(UserCreationForm):
    """
    docstring
    """
    class Meta:
        
        model = User
        fields = ('username', 'email', 'password1', 'password2','first_name', 'last_name')
        exclude= ('email',)


    # username = forms.EmailField(max_length=64,
    #     help_text = "The person's email address.")

    # def clean_email( self ):
    #     email= self.cleaned_data['username']
    #     return email


        
        
