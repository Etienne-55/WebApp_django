from django import forms
from .models import Coffee 

class cofee_form(forms.ModelForm):
    class Meta:
        model = Coffee 
        fields = ('name', 'origin', 'roast')