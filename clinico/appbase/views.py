from datetime import datetime
from threading import local

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from appconsulta.forms import RecetaForm
from appconsulta.models import Receta
from .models import *
from .forms import *


# Vista de Inicio


@method_decorator(login_required(login_url='/seguridad/login/'), name="dispatch")
class InicioV2(TemplateView):
    template_name = "Menu.html"


# Vista de Inicio de Secion

class login_session_View(View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'seguridad/Login.html'

    def post(self, request, *args, **kwargs):
        data = {}
        user = authenticate(username=request.POST['usuario'],
                            password=request.POST['password'])
        data['resp'] = False
        if user is not None:
            if user.is_active:
                login(request, user)
                data['resp'] = True
                data['user'] = user.username
                data['activo'] = ''
                data['fechaactual'] = datetime.now()
            else:
                data['error'] = 'Usuario no esta Activo'
        else:
            data['valcodigo'] = 1
            data['error'] = 'El usuario o contraseña estan incorrectos'
        return JsonResponse(data, safe=False)

    def get(self, request, *args, **kwargs):
        data = {
            'activo': 'hidden'
        }
        return render(request, self.template_name, data)


class logout_user(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/seguridad/login/')


# Vista de Pacientes
#    Lista los registros de los pacientes
class PacienteView(ListView):
    model = Paciente
    template_name = "base/paciente/ListPaciente.html"
    context_object_name = "pacientes"

    # queryset = Paciente.objects.filter(estado=False)

    def get_queryset(self):
        nombre = self.request.GET.get('nombre') if self.request.GET.get('nombre') else ''
        return self.model.objects.filter(nombre__icontains=nombre, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''
        context['titulo'] = "Consulta de pacientes"
        return context


# Doctor
class DoctorView(ListView):
    model = Doctor
    template_name = "base/doctor/ListDoctor.html"
    context_object_name = "doctores"

    # queryset = Paciente.objects.filter(estado=False)

    def get_queryset(self):
        nombre = self.request.GET.get('nombre') if self.request.GET.get('nombre') else ''
        return self.model.objects.filter(nombre__icontains=nombre, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''
        context['titulo'] = "Consulta de pacientes"
        return context


#    Crea un nuevo registro de los pacientes


class CrearPacienteView(CreateView):
    model = Paciente
    # fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/paciente/PacienteMantenimiento.html"
    form_class = PacienteForm
    success_url = reverse_lazy('base:paciente')
    context_object_name = "pacientes"


class CrearDoctorView(CreateView):
    model = Doctor
    # fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/doctor/ManDoctor.html"
    form_class = DoctorForm
    success_url = reverse_lazy('base:doctor')
    context_object_name = "doctores"


#    Edita o modifica  un registro de los pacientes


#    Edita o modifica  un registro de los pacientes


class EditarPacienteView(UpdateView):
    model = Paciente
    # fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/paciente/PacienteMantenimiento.html"
    form_class = PacienteForm
    success_url = reverse_lazy('base:paciente')
    context_object_name = "pacientes"


class EditarDoctorView(UpdateView):
    model = Doctor
    # fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/doctor/ManDoctor.html"
    form_class = DoctorForm
    success_url = reverse_lazy('base:doctor')
    context_object_name = "doctores"


class EliminarPacienteView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            paciente = Paciente.objects.get(id=pk)
            paciente.delete()
            # object.estado = False
            # object.save()
            return redirect('base:paciente')
        except Exception as e:
            return redirect('base:paciente')


class EliminarDoctorView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            doctor = Doctor.objects.get(id=pk)
            doctor.delete()
            # object.estado = False
            # object.save()
            return redirect('base:doctor')
        except Exception as e:
            return redirect('base:doctor')


# Configuracion
class InicioConfiguracion(TemplateView):
    template_name = "base/configuracion/Configuracion.html"


# Provincia
class ConfiguracionListView(ListView):
    model = Provincia
    template_name = "base/configuracion/ListProvincia.html"
    context_object_name = "provincias"

    # queryset = Paciente.objects.filter(estado=False)

    def get_queryset(self):
        descripcion = self.request.GET.get('descripcion') if self.request.GET.get('descripcion') else ''
        return self.model.objects.filter(descripcion__icontains=descripcion, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'descripcion') if self.request.GET.get('descripcion') else ''
        context['titulo'] = "Consulta de Provincias"
        context['modulo'] = "Provincia"
        return context


class CrearProvinciaView(CreateView):
    model = Provincia
    template_name = "base/configuracion/ManProvincia.html"
    form_class = ProvinciaForm
    success_url = reverse_lazy('base:configuracion_listap')
    context_object_name = "provincias"


class EditarProvinciaView(UpdateView):
    model = Provincia
    template_name = "base/configuracion/ManProvincia.html"
    form_class = ProvinciaForm
    success_url = reverse_lazy('base:configuracion_listap')
    context_object_name = "provincias"


class EliminarProvinciaView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            provincia = Provincia.objects.get(id=pk)
            provincia.delete()
            # object.estado = False
            # object.save()
            return redirect('base:configuracion_listap')
        except Exception as e:
            return redirect('base:configuracion_listap')


# Ciudad
class ConfiguracionListCiudadView(ListView):
    model = Ciudad
    template_name = "base/configuracion/ListCiudad.html"
    context_object_name = "ciudades"

    # queryset = Paciente.objects.filter(estado=False)

    def get_queryset(self):
        descripcion = self.request.GET.get('descripcion') if self.request.GET.get('descripcion') else ''
        return self.model.objects.filter(descripcion__icontains=descripcion, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'descripcion') if self.request.GET.get('descripcion') else ''
        context['titulo'] = "Consulta de Ciudades"
        context['modulo'] = "Ciudad"
        return context


class CrearCiudadView(CreateView):
    model = Ciudad
    template_name = "base/configuracion/ManCiudad.html"
    form_class = CiudadForm
    success_url = reverse_lazy('base:configuracion_listac')
    context_object_name = "ciudades"


class EditarCiudadView(UpdateView):
    model = Ciudad
    template_name = "base/configuracion/ManCiudad.html"
    form_class = CiudadForm
    success_url = reverse_lazy('base:configuracion_listac')
    context_object_name = "ciudades"


class EliminarCiudadView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            ciudad = Ciudad.objects.get(id=pk)
            ciudad.delete()
            # object.estado = False
            # object.save()
            return redirect('base:configuracion_listac')
        except Exception as e:
            return redirect('base:configuracion_listac')


# Profesion
class ConfiguracionListProfesiondView(ListView):
    model = Profesion
    template_name = "base/configuracion/ListProfesion.html"
    context_object_name = "profesiones"

    def get_queryset(self):
        descripcion = self.request.GET.get('descripcion') if self.request.GET.get('descripcion') else ''
        return self.model.objects.filter(descripcion__icontains=descripcion, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'descripcion') if self.request.GET.get('descripcion') else ''
        context['titulo'] = "Consulta de Profesiones"
        context['modulo'] = "Profesion"
        return context


class CrearProfesionView(CreateView):
    model = Profesion
    template_name = "base/configuracion/ManProfesion.html"
    form_class = ProfesionForm
    success_url = reverse_lazy('base:configuracion_listapro')
    context_object_name = "profesiones"


class EditarProfesionView(UpdateView):
    model = Profesion
    template_name = "base/configuracion/ManProfesion.html"
    form_class = ProfesionForm
    success_url = reverse_lazy('base:configuracion_listapro')
    context_object_name = "profesiones"


class EliminarProfesionView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            profesion = Profesion.objects.get(id=pk)
            profesion.delete()
            # object.estado = False
            # object.save()
            return redirect('base:configuracion_listapro')
        except Exception as e:
            return redirect('base:configuracion_listapro')


# Profesion
class ConfiguracionListTituloView(ListView):
    model = Titulo
    template_name = "base/configuracion/ListTitulo.html"
    context_object_name = "titulos"

    def get_queryset(self):
        descripcion = self.request.GET.get('descripcion') if self.request.GET.get('descripcion') else ''
        return self.model.objects.filter(descripcion__icontains=descripcion, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'descripcion') if self.request.GET.get('descripcion') else ''
        context['titulo'] = "Consulta de Profesiones"
        context['modulo'] = "Profesion"
        return context


class CrearTituloView(CreateView):
    model = Titulo
    template_name = "base/configuracion/ManTitulo.html"
    form_class = TituloForm
    success_url = reverse_lazy('base:configuracion_listati')
    context_object_name = "titulos"


class EditarTituloView(UpdateView):
    model = Titulo
    template_name = "base/configuracion/ManTitulo.html"
    form_class = TituloForm
    success_url = reverse_lazy('base:configuracion_listati')
    context_object_name = "titulos"


class EliminarTituloView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            titulo = Titulo.objects.get(id=pk)
            titulo.delete()
            # object.estado = False
            # object.save()
            return redirect('base:configuracion_listati')
        except Exception as e:
            return redirect('base:configuracion_listati')


# Sangre
class ConfiguracionListSangreView(ListView):
    model = Sangre
    template_name = "base/configuracion/ListSangre.html"
    context_object_name = "sangres"

    def get_queryset(self):
        descripcion = self.request.GET.get('tipo') if self.request.GET.get('tipo') else ''
        return self.model.objects.filter(tipo__icontains=descripcion, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'tipo') if self.request.GET.get('tipo') else ''
        context['titulo'] = "Consulta de Sangre"
        context['modulo'] = "Sangre"
        return context


class CrearSangreView(CreateView):
    model = Sangre
    template_name = "base/configuracion/ManSangre.html"
    form_class = SangreForm
    success_url = reverse_lazy('base:configuracion_listasa')
    context_object_name = "sangres"


class EditarSangreView(UpdateView):
    model = Sangre
    template_name = "base/configuracion/ManSangre.html"
    form_class = SangreForm
    success_url = reverse_lazy('base:configuracion_listasa')
    context_object_name = "sangres"


class EliminarSangreView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            sangre = Sangre.objects.get(id=pk)
            sangre.delete()
            # object.estado = False
            # object.save()
            return redirect('base:configuracion_listasa')
        except Exception as e:
            return redirect('base:configuracion_listasa')


# Horario
class ConfiguracionListHorarioView(ListView):
    model = Horario
    template_name = "base/configuracion/ListHorario.html"
    context_object_name = "horarios"

    def get_queryset(self):
        descripcion = self.request.GET.get('dia') if self.request.GET.get('dia') else ''
        return self.model.objects.filter(dia__icontains=descripcion, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'dia') if self.request.GET.get('dia') else ''
        context['titulo'] = "Consulta de Horario"
        context['modulo'] = "Horario"
        return context


class CrearHorarioView(CreateView):
    model = Horario
    template_name = "base/configuracion/ManHorario.html"
    form_class = HorarioForm
    success_url = reverse_lazy('base:configuracion_listaho')
    context_object_name = "horarios"


class EditarHorarioView(UpdateView):
    model = Horario
    template_name = "base/configuracion/ManHorario.html"
    form_class = HorarioForm
    success_url = reverse_lazy('base:configuracion_listaho')
    context_object_name = "horarios"


class EliminarHorarioView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            horario = Horario.objects.get(id=pk)
            horario.delete()
            # object.estado = False
            # object.save()
            return redirect('base:configuracion_listaho')
        except Exception as e:
            return redirect('base:configuracion_listaho')


# Grupo Antecedente
class ConfiguracionListGAntecedenteView(ListView):
    model = GrupoAntecedente
    template_name = "base/configuracion/ListGAntecedente.html"
    context_object_name = "gantecedentes"

    def get_queryset(self):
        descripcion = self.request.GET.get('descripcion') if self.request.GET.get('descripcion') else ''
        return self.model.objects.filter(descripcion__icontains=descripcion, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'descripcion') if self.request.GET.get('descripcion') else ''
        context['titulo'] = "Consulta de Grupo Antecedete"
        return context


class CrearGAntecedenteView(CreateView):
    model = GrupoAntecedente
    template_name = "base/configuracion/ManGAntecedente.html"
    form_class = GAntecedenteForm
    success_url = reverse_lazy('base:configuracion_listaga')
    context_object_name = "gantecedentes"


class EditarGAntecedenteView(UpdateView):
    model = GrupoAntecedente
    template_name = "base/configuracion/ManGAntecedente.html"
    form_class = GAntecedenteForm
    success_url = reverse_lazy('base:configuracion_listaga')
    context_object_name = "gantecedentes"


class EliminarGAntecedenteView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            gantecedente = GrupoAntecedente.objects.get(id=pk)
            gantecedente.delete()
            # object.estado = False
            # object.save()
            return redirect('base:configuracion_listaga')
        except Exception as e:
            return redirect('base:configuracion_listaga')


# Grupo Antecedente
class ConfiguracionListAntecedenteView(ListView):
    model = Antecedente
    template_name = "base/configuracion/ListAntecedente.html"
    context_object_name = "antecedentes"

    def get_queryset(self):
        descripcion = self.request.GET.get('descripcion') if self.request.GET.get('descripcion') else ''
        return self.model.objects.filter(descripcion__icontains=descripcion, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'descripcion') if self.request.GET.get('descripcion') else ''
        context['titulo'] = "Consulta de Grupo Antecedete"
        return context


class CrearAntecedenteView(CreateView):
    model = Antecedente
    template_name = "base/configuracion/ManAntecedente.html"
    form_class = AntecedenteForm
    success_url = reverse_lazy('base:configuracion_listaa')
    context_object_name = "antecedentes"


class EditarAntecedenteView(UpdateView):
    model = Antecedente
    template_name = "base/configuracion/ManAntecedente.html"
    form_class = AntecedenteForm
    success_url = reverse_lazy('base:configuracion_listaa')
    context_object_name = "antecedentes"


class EliminarAntecedenteView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            antecedente = Antecedente.objects.get(id=pk)
            antecedente.delete()
            # object.estado = False
            # object.save()
            return redirect('base:configuracion_listaa')
        except Exception as e:
            return redirect('base:configuracion_listaa')


# Grupo Medicamento
class ConfiguracionListMedicamentoView(ListView):
    model = Medicamento
    template_name = "base/configuracion/ListMedicamento.html"
    context_object_name = "medicamentos"

    def get_queryset(self):
        descripcion = self.request.GET.get('descripcion') if self.request.GET.get('descripcion') else ''
        return self.model.objects.filter(descripcion__icontains=descripcion, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'descripcion') if self.request.GET.get('descripcion') else ''
        context['titulo'] = "Consulta de Medicamento"
        return context


class CrearMedicamentoView(CreateView):
    model = Medicamento
    template_name = "base/configuracion/ManMedicamento.html"
    form_class = MedicamentoForm
    success_url = reverse_lazy('base:configuracion_listame')
    context_object_name = "medicamentos"


class EditarMedicamentoView(UpdateView):
    model = Medicamento
    template_name = "base/configuracion/ManMedicamento.html"
    form_class = MedicamentoForm
    success_url = reverse_lazy('base:configuracion_listame')
    context_object_name = "medicamentos"


class EliminarMedicamentoView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            medicamentos = Medicamento.objects.get(id=pk)
            medicamentos.delete()
            # object.estado = False
            # object.save()
            return redirect('base:configuracion_listame')
        except Exception as e:
            return redirect('base:configuracion_listame')


# Grupo Frecuencia
class ConfiguracionListFrecuenciaView(ListView):
    model = Frecuencia
    template_name = "base/configuracion/ListFrecuencia.html"
    context_object_name = "frecuencias"

    def get_queryset(self):
        descripcion = self.request.GET.get('descripcion') if self.request.GET.get('descripcion') else ''
        return self.model.objects.filter(descripcion__icontains=descripcion, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'descripcion') if self.request.GET.get('descripcion') else ''
        context['titulo'] = "Consulta de Medicamento"
        return context


class CrearFrecuenciaView(CreateView):
    model = Frecuencia
    template_name = "base/configuracion/ManFrecuencia.html"
    form_class = FrecuenciaForm
    success_url = reverse_lazy('base:configuracion_listafe')
    context_object_name = "frecuencias"


class EditarFrecuenciaView(UpdateView):
    model = Frecuencia
    template_name = "base/configuracion/ManFrecuencia.html"
    form_class = FrecuenciaForm
    success_url = reverse_lazy('base:configuracion_listafe')
    context_object_name = "frecuencias"


class EliminarFrecuenciaView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            frecuencia = Frecuencia.objects.get(id=pk)
            frecuencia.delete()
            # object.estado = False
            # object.save()
            return redirect('base:configuracion_listafe')
        except Exception as e:
            return redirect('base:configuracion_listafe')


# Grupo Dosis
class ConfiguracionListDosisView(ListView):
    model = Dosis
    template_name = "base/configuracion/ListDosis.html"
    context_object_name = "dosis"

    def get_queryset(self):
        descripcion = self.request.GET.get('descripcion') if self.request.GET.get('descripcion') else ''
        return self.model.objects.filter(descripcion__icontains=descripcion, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'descripcion') if self.request.GET.get('descripcion') else ''
        context['titulo'] = "Consulta de Medicamento"
        return context


class CrearDosisView(CreateView):
    model = Dosis
    template_name = "base/configuracion/ManDosis.html"
    form_class = DosisForm
    success_url = reverse_lazy('base:configuracion_listado')
    context_object_name = "dosis"


class EditarDosisView(UpdateView):
    model = Dosis
    template_name = "base/configuracion/ManDosis.html"
    form_class = DosisForm
    success_url = reverse_lazy('base:configuracion_listado')
    context_object_name = "dosis"


class EliminarDosisView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            dosis = Dosis.objects.get(id=pk)
            dosis.delete()
            # object.estado = False
            # object.save()
            return redirect('base:configuracion_listado')
        except Exception as e:
            return redirect('base:configuracion_listado')


# Grupo Duracion
class ConfiguracionListDuracionView(ListView):
    model = Duracion
    template_name = "base/configuracion/ListDuracion.html"
    context_object_name = "duracion"

    def get_queryset(self):
        descripcion = self.request.GET.get('descripcion') if self.request.GET.get('descripcion') else ''
        return self.model.objects.filter(descripcion__icontains=descripcion, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'descripcion') if self.request.GET.get('descripcion') else ''
        context['titulo'] = "Consulta de Medicamento"
        return context


class CrearDuracionView(CreateView):
    model = Duracion
    template_name = "base/configuracion/ManDuracion.html"
    form_class = DuracionForm
    success_url = reverse_lazy('base:configuracion_listadu')
    context_object_name = "duracion"


class EditarDuracionView(UpdateView):
    model = Duracion
    template_name = "base/configuracion/ManDuracion.html"
    form_class = DuracionForm
    success_url = reverse_lazy('base:configuracion_listadu')
    context_object_name = "duracion"


class EliminarDuracionView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            duracion = Duracion.objects.get(id=pk)
            duracion.delete()
            # object.estado = False
            # object.save()
            return redirect('base:configuracion_listadu')
        except Exception as e:
            return redirect('base:configuracion_listadu')


# Grupo Sintoma
class ConfiguracionListSintomaView(ListView):
    model = Sintoma
    template_name = "base/configuracion/ListSintoma.html"
    context_object_name = "sintomas"

    def get_queryset(self):
        descripcion = self.request.GET.get('descripcion') if self.request.GET.get('descripcion') else ''
        return self.model.objects.filter(descripcion__icontains=descripcion, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'descripcion') if self.request.GET.get('descripcion') else ''
        context['titulo'] = "Consulta de Medicamento"
        return context


class CrearSintomaView(CreateView):
    model = Sintoma
    template_name = "base/configuracion/ManSintoma.html"
    form_class = SintomaForm
    success_url = reverse_lazy('base:configuracion_listasin')
    context_object_name = "sintomas"


class EditarSintomaView(UpdateView):
    model = Sintoma
    template_name = "base/configuracion/ManSintoma.html"
    form_class = SintomaForm
    success_url = reverse_lazy('base:configuracion_listasin')
    context_object_name = "sintomas"


class EliminarSintomaView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            sintoma = Sintoma.objects.get(id=pk)
            sintoma.delete()
            # object.estado = False
            # object.save()
            return redirect('base:configuracion_listasin')
        except Exception as e:
            return redirect('base:configuracion_listasin')


# Grupo Diagnostico
class ConfiguracionListDiagnosticoView(ListView):
    model = Diagnostico
    template_name = "base/configuracion/ListDiagnostico.html"
    context_object_name = "diagnosticos"

    def get_queryset(self):
        descripcion = self.request.GET.get('descripcion') if self.request.GET.get('descripcion') else ''
        return self.model.objects.filter(descripcion__icontains=descripcion, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'descripcion') if self.request.GET.get('descripcion') else ''
        context['titulo'] = "Consulta de Medicamento"
        return context


class CrearDiagnosticoView(CreateView):
    model = Diagnostico
    template_name = "base/configuracion/ManDiagnostico.html"
    form_class = DiagnosticoForm
    success_url = reverse_lazy('base:configuracion_listadia')
    context_object_name = "diagnosticos"


class EditarDiagnosticoView(UpdateView):
    model = Diagnostico
    template_name = "base/configuracion/ManDiagnostico.html"
    form_class = DiagnosticoForm
    success_url = reverse_lazy('base:configuracion_listadia')
    context_object_name = "diagnosticos"


class EliminarDiagnosticoView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            sintoma = Diagnostico.objects.get(id=pk)
            sintoma.delete()
            # object.estado = False
            # object.save()
            return redirect('base:configuracion_listadia')
        except Exception as e:
            return redirect('base:configuracion_listadia')


#  SignoVital
class ConfiguracionListSignoVitalView(ListView):
    model = SignoVital
    template_name = "base/configuracion/ListSignoVital.html"
    context_object_name = "signosvitales"

    def get_queryset(self):
        descripcion = self.request.GET.get('descripcion') if self.request.GET.get('descripcion') else ''
        return self.model.objects.filter(descripcion__icontains=descripcion, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'descripcion') if self.request.GET.get('descripcion') else ''
        context['titulo'] = "Consulta de Medicamento"
        return context


class CrearSignoVitalView(CreateView):
    model = SignoVital
    template_name = "base/configuracion/ManSignoVital.html"
    form_class = SignoVitalForm
    success_url = reverse_lazy('base:configuracion_listasv')
    context_object_name = "signosvitales"


class EditarSignoVitalView(UpdateView):
    model = SignoVital
    template_name = "base/configuracion/ManSignoVital.html"
    form_class = SignoVitalForm
    success_url = reverse_lazy('base:configuracion_listasv')
    context_object_name = "signosvitales"


class EliminarSignoVitalView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            sintoma = SignoVital.objects.get(id=pk)
            sintoma.delete()
            # object.estado = False
            # object.save()
            return redirect('base:configuracion_listasv')
        except Exception as e:
            return redirect('base:configuracion_listasv')


#  EstudioGabinete
class ConfiguracionListEstudioGabineteView(ListView):
    model = EstudioGabinete
    template_name = "base/configuracion/ListEstudioGabinete.html"
    context_object_name = "estudiogabinete"

    def get_queryset(self):
        descripcion = self.request.GET.get('descripcion') if self.request.GET.get('descripcion') else ''
        return self.model.objects.filter(descripcion__icontains=descripcion, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'descripcion') if self.request.GET.get('descripcion') else ''
        context['titulo'] = "Consulta de Medicamento"
        return context


class CrearEstudioGabineteView(CreateView):
    model = EstudioGabinete
    template_name = "base/configuracion/ManEstudioGabinete.html"
    form_class = EstudioGabineteForm
    success_url = reverse_lazy('base:configuracion_listaseg')
    context_object_name = "estudiogabinete"


class EditarEstudioGabineteView(UpdateView):
    model = EstudioGabinete
    template_name = "base/configuracion/ManEstudioGabinete.html"
    form_class = EstudioGabineteForm
    success_url = reverse_lazy('base:configuracion_listaseg')
    context_object_name = "estudiogabinete"


class EliminarEstudioGabineteView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            sintoma = EstudioGabinete.objects.get(id=pk)
            sintoma.delete()
            # object.estado = False
            # object.save()
            return redirect('base:configuracion_listaseg')
        except Exception as e:
            return redirect('base:configuracion_listaseg')


# Agenda
class AgendaView(ListView):
    model = Agenda
    template_name = "Atencion/agenda/Agenda.html"
    context_object_name = "agendas"

    def get_queryset(self):
        descripcion = self.request.GET.get('fecha') if self.request.GET.get('fecha') else ''
        return self.model.objects.filter(fecha__icontains=descripcion, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'fecha') if self.request.GET.get('fecha') else ''
        context['titulo'] = "Consulta de paciente"
        return context


# Cita
class CitaView(CreateView):
    model = Agenda
    template_name = "Atencion/agenda/Cita.html"
    form_class = AgendaForm
    success_url = reverse_lazy('base:agenda')
    context_object_name = "agendas"


class EditarcitaView(UpdateView):
    model = Agenda
    template_name = "Atencion/agenda/Cita.html"
    form_class = AgendaForm
    success_url = reverse_lazy('base:agenda')
    context_object_name = "agendas"


class EliminarcitaView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            sintoma = Agenda.objects.get(id=pk)
            sintoma.delete()
            # object.estado = False
            # object.save()
            return redirect('base:agenda')
        except Exception as e:
            return redirect('base:agenda')
