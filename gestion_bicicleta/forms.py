from django import forms
from .models import Bicicleta

class BicicletaForm(forms.ModelForm):
    """
    docstring
    """
    class Meta:
        
        model = Bicicleta
        
        fields = ['codigo', 'estacion'  , 'estado']
    
      
    def __init__(self, *args , **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control" 


class BicicletaListForm(forms.ModelForm):
    """
    docstring
    """
    class Meta:
        
        model = Bicicleta
        
        fields = ['codigo', 'estacion' ]
    
      
    def __init__(self, *args , **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control" 

