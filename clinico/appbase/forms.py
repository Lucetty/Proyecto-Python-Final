from django import forms
from django.db.models import fields
from .models import *


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        # fields = ('nombre', 'apellido', 'cedula')
        # label = {
        #     'nombre': 'Nombres',
        #     'apellido': 'Apellidos',
        #     'cedula': 'Cedula'
        # }
        fields = '__all__'
        widgets = {
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nacimiento': forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'civil': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'profesion': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'titulo': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'provincia': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sangre': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'hijos': forms.NumberInput(
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


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        # fields = ('nombre', 'apellido', 'cedula')
        # label = {
        #     'nombre': 'Nombres',
        #     'apellido': 'Apellidos',
        #     'cedula': 'Cedula'
        # }
        fields = '__all__'
        widgets = {
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nacimiento': forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'civil': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'profesion': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'titulo': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'provincia': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'consultorio': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'lugar': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'logo': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'horario': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'registro': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'duracion': forms.TextInput(
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


class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        # fields = ('nombre', 'apellido', 'cedula')
        # label = {
        #     'nombre': 'Nombres',
        #     'apellido': 'Apellidos',
        #     'cedula': 'Cedula'
        # }
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(
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


class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        # fields = ('nombre', 'apellido', 'cedula')
        # label = {
        #     'nombre': 'Nombres',
        #     'apellido': 'Apellidos',
        #     'cedula': 'Cedula'
        # }
        fields = '__all__'
        widgets = {
            'provincia': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'descripcion': forms.TextInput(
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


class ProfesionForm(forms.ModelForm):
    class Meta:
        model = Profesion
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(
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


class TituloForm(forms.ModelForm):
    class Meta:
        model = Titulo
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(
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


class SangreForm(forms.ModelForm):
    class Meta:
        model = Sangre
        fields = '__all__'
        widgets = {
            'tipo': forms.TextInput(
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


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'
        widgets = {
            'dia': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'desde': forms.TimeInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'hasta': forms.TimeInput(
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
class GAntecedenteForm(forms.ModelForm):
    class Meta:
        model = GrupoAntecedente
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(
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

class AntecedenteForm(forms.ModelForm):
    class Meta:
        model = Antecedente
        fields = '__all__'
        widgets = {
            'grupoAntecedente': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'descripcion': forms.TextInput(
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

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = '__all__'
        widgets = {
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'descripcion': forms.TextInput(
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

class FrecuenciaForm(forms.ModelForm):
    class Meta:
        model = Frecuencia
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(
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

class DosisForm(forms.ModelForm):
    class Meta:
        model = Dosis
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(
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

class DuracionForm(forms.ModelForm):
    class Meta:
        model = Duracion
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(
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

class SintomaForm(forms.ModelForm):
    class Meta:
        model = Sintoma
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(
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

class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = '__all__'
        widgets = {
            'codigo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'descripcion': forms.TextInput(
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

class SignoVitalForm(forms.ModelForm):
    class Meta:
        model = SignoVital
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'rango1': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'rango2': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'medida': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'imagen': forms.FileInput(
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

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = '__all__'
        widgets = {
            'paciente': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'fecha': forms.DateInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'hora': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'type' : 'time',
                }
            ),
            'motivo': forms.TextInput(
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

class EstudioGabineteForm(forms.ModelForm):
    class Meta:
        model = EstudioGabinete
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(
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

