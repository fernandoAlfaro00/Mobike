from django import forms
from .models import Cliente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class ClienteForm(forms.ModelForm):
    """
    docstring
    """
    class Meta:
        
        model = Cliente
        
        fields = '__all__'
        exclude  = ['user']
        labels = {
            'tarjeta' : 'N° tarjeta', 
            'fecha_nac' : 'Fecha nacimiento',
        }
        widgets  = {
            'fecha_nac' : forms.DateInput(attrs={'type': 'date'}), 
        }
    def __init__(self, *args , **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
        
            field.widget.attrs["class"] = "form-control"




class UserForm(UserCreationForm):
    """
    docstring
    """

    
    class Meta:
        
        model = User
        fields = ('username', 'email', 'password1','first_name', 'last_name')




    def __init__(self, *args , **kwargs):
        super().__init__(*args,**kwargs)
        self.fields.pop('password2')
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control" 
