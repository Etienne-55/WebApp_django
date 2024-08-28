from django import forms
from .models import computer_hardware

class computer_hardware_form(forms.ModelForm):
    class Meta:
        model = computer_hardware
        fields = ('name', 'id_number', 'price', 'quantity')