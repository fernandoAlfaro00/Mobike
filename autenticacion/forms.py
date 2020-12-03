from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


class PUserForm(UserCreationForm):
    """
    docstring
    """
    class Meta:
        
        model = User
        fields = ('username', 'first_name' , 'last_name',  'password1', 'password2' , 'email')
        # exclude= ('email',)


    # username = forms.EmailField(max_length=64,
    #     help_text = "The person's email address.")

    # def clean_email( self ):
    #     email= self.cleaned_data['username']
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError("EL Email ya existe")
    #     return email

        