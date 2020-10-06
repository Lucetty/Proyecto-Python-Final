from django import forms
from django.db.models import fields
from .models import *


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = '__all__'
        widgets = {
            'paciente': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'fecha': forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'hora': forms.TimeInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'motivo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sintoma': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'exploracion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'diagnostico': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'gabinete': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'instrucciones': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class DetalleRecetaForm(forms.ModelForm):
    class Meta:
        model = DetalleReceta
        fields = '__all__'
        widgets = {
            'receta': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'medicamento': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'medicamento': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'cantidad': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': 1
                }
            ),
            'dosis': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'frecuencia': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'duracion': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

class TomarSignoVitalForm(forms.ModelForm):
    class Meta:
        model = TomarSignoVital
        fields = '__all__'
        widgets = {
            'receta': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'signovital': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'valor': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
