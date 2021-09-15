from django import forms
from .models import Postagem 

class PostForms(forms.ModelForm):
    class Meta:
        model = Postagem 
        fields = ('titulo','texto')



