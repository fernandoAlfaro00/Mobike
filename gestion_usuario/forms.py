from django import forms
from .models import  Funcionario
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm



class FuncionarioForm(forms.ModelForm):
    """
    docstring
    """
    class Meta:
        
        model = Funcionario
        
        fields = '__all__'
        exclude  = ['user']
        widgets = {
                        
            'area' : forms.TextInput(attrs={'class':'form-control' , 'type':'text'}),
 
            'genero' : forms.Select(attrs={'class':'form-control'}),
        }


class UserForm(UserCreationForm):
    """
    docstring
    """

    
    class Meta:
        
        model = User
        fields = ('username', 'email', 'password1','first_name', 'last_name' , 'is_active')




    def __init__(self, *args , **kwargs):
        super().__init__(*args,**kwargs)
        self.fields.pop('password2')
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control" 





class UserModForm(forms.ModelForm):
    """
    docstring
    """

    
    class Meta:
        
        model = User
        fields = ('username', 'email','first_name', 'last_name' , 'is_active')
        



    def __init__(self, *args , **kwargs):
        super().__init__(*args,**kwargs)
        
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control" 
