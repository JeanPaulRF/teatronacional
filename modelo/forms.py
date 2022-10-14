from django.forms import ModelForm
from .models import Usuario


class SigninForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'contrasena']
    