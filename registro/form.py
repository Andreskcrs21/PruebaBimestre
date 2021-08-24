from django import forms
from  .models import UsuarioEquipos


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = UsuarioEquipos
        fields = '__all__'