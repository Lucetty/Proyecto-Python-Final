from django.urls import path
from .views import *

app_name = 'base'
urlpatterns = [
    # Paciente
    path('paciente/', PacienteView.as_view(), name='paciente'),
    path('crear_paciente/', CrearPacienteView.as_view(), name='crear_paciente'),
    path('editar_paciente/<int:pk>/',
         EditarPacienteView.as_view(), name='editar_paciente'),
    path('eliminar_paciente/<int:pk>/',
         EliminarPacienteView.as_view(), name='eliminar_paciente'),
    # Doctor
    path('Doctor/', DoctorView.as_view(), name='doctor'),
    path('crear_doctor/', CrearDoctorView.as_view(), name='crear_doctor'),
    path('editar_doctor/<int:pk>/', EditarDoctorView.as_view(), name='editar_doctor'),
    path('eliminar_doctor/<int:pk>/',
         EliminarDoctorView.as_view(), name='eliminar_doctor'),
    # Configuracion
    path('Configuracion/', InicioConfiguracion.as_view(), name='configuracion'),

    # Provincia
    path('Configuracion/Lista/Provincia/', ConfiguracionListView.as_view(), name='configuracion_listap'),
    path('Configuracion/Lista/Provincia/Nuevo', CrearProvinciaView.as_view(), name='crear_provincia'),
    path('Configuracion/Lista/Provincia/editar_provincia/<int:pk>/', EditarProvinciaView.as_view(),
         name='editar_provincia'),
    path('Configuracion/Lista/Provincia/eliminar_provincia/<int:pk>/',
         EliminarProvinciaView.as_view(), name='eliminar_provincia'),

    # Ciudad
    path('Configuracion/Lista/Ciudad/', ConfiguracionListCiudadView.as_view(), name='configuracion_listac'),
    path('Configuracion/Lista/Ciudad/Nuevo', CrearCiudadView.as_view(), name='crear_ciudad'),
    path('Configuracion/Lista/Ciudad/editar_ciudad/<int:pk>/', EditarCiudadView.as_view(),
         name='editar_ciudad'),
    path('Configuracion/Lista/Ciudad/eliminar_ciudad/<int:pk>/',
         EliminarCiudadView.as_view(), name='eliminar_ciudad'),

    # Profesion
    path('Configuracion/Lista/Profesion/', ConfiguracionListProfesiondView.as_view(), name='configuracion_listapro'),
    path('Configuracion/Lista/Profesion/Nuevo', CrearProfesionView.as_view(), name='crear_profesion'),
    path('Configuracion/Lista/Profesion/editar_profesion/<int:pk>/', EditarProfesionView.as_view(),
         name='editar_profesion'),
    path('Configuracion/Lista/Profesion/eliminar_profesion/<int:pk>/',
         EliminarProfesionView.as_view(), name='eliminar_profesion'),

    # Titulo
    path('Configuracion/Lista/Titulo/', ConfiguracionListTituloView.as_view(), name='configuracion_listati'),
    path('Configuracion/Lista/Titulo/Nuevo', CrearTituloView.as_view(), name='crear_titulo'),
    path('Configuracion/Lista/Titulo/editar_titulo/<int:pk>/', EditarTituloView.as_view(),
         name='editar_titulo'),
    path('Configuracion/Lista/Titulo/eliminar_titulo/<int:pk>/',
         EliminarTituloView.as_view(), name='eliminar_titulo'),
    # Sangre
    path('Configuracion/Lista/Sangre/', ConfiguracionListSangreView.as_view(), name='configuracion_listasa'),
    path('Configuracion/Lista/Sangre/Nuevo', CrearSangreView.as_view(), name='crear_sangre'),
    path('Configuracion/Lista/Sangre/editar_titulo/<int:pk>/', EditarSangreView.as_view(),
         name='editar_sangre'),
    path('Configuracion/Lista/Sangre/eliminar_titulo/<int:pk>/',
         EliminarSangreView.as_view(), name='eliminar_sangre'),

    # Horario
    path('Configuracion/Lista/Horario/', ConfiguracionListHorarioView.as_view(), name='configuracion_listaho'),
    path('Configuracion/Lista/Horario/Nuevo', CrearHorarioView.as_view(), name='crear_horario'),
    path('Configuracion/Lista/Horario/editar_horario/<int:pk>/', EditarHorarioView.as_view(),
         name='editar_horario'),
    path('Configuracion/Lista/Horario/eliminar_horario/<int:pk>/',
         EliminarHorarioView.as_view(), name='eliminar_horario'),
    # Grupo Antecedente
    path('Configuracion/Lista/Grupo_Antecedente/', ConfiguracionListGAntecedenteView.as_view(),
         name='configuracion_listaga'),
    path('Configuracion/Lista/Grupo_Antecedente/Nuevo', CrearGAntecedenteView.as_view(), name='crear_gantecedente'),
    path('Configuracion/Lista/Grupo_Antecedente/editar_gantecedente/<int:pk>/', EditarGAntecedenteView.as_view(),
         name='editar_gantecedente'),
    path('Configuracion/Lista/Grupo_Antecedente/eliminar_gantecedente/<int:pk>/',
         EliminarGAntecedenteView.as_view(), name='eliminar_gantecedente'),

    #  Antecedente
    path('Configuracion/Lista/Antecedente/', ConfiguracionListAntecedenteView.as_view(),
         name='configuracion_listaa'),
    path('Configuracion/Lista/Antecedente/Nuevo', CrearAntecedenteView.as_view(), name='crear_antecedente'),
    path('Configuracion/Lista/Antecedente/editar_antecedente/<int:pk>/', EditarAntecedenteView.as_view(),
         name='editar_antecedente'),
    path('Configuracion/Lista/Antecedente/eliminar_antecedente/<int:pk>/',
         EliminarAntecedenteView.as_view(), name='eliminar_antecedente'),

    #  Medicamento
    path('Configuracion/Lista/Medicamento/', ConfiguracionListMedicamentoView.as_view(),
         name='configuracion_listame'),
    path('Configuracion/Lista/Medicamento/Nuevo', CrearMedicamentoView.as_view(), name='crear_medicamento'),
    path('Configuracion/Lista/Medicamento/editar_medicamento/<int:pk>/', EditarMedicamentoView.as_view(),
         name='editar_medicamento'),
    path('Configuracion/Lista/Medicamento/eliminar_medicamento/<int:pk>/',
         EliminarMedicamentoView.as_view(), name='eliminar_medicamento'),

    #  Frecuencia
    path('Configuracion/Lista/Frecuencia/', ConfiguracionListFrecuenciaView.as_view(),
         name='configuracion_listafe'),
    path('Configuracion/Lista/Frecuencia/Nuevo', CrearFrecuenciaView.as_view(), name='crear_frecuencia'),
    path('Configuracion/Lista/Frecuencia/editar_frecuencia/<int:pk>/', EditarFrecuenciaView.as_view(),
         name='editar_frecuencia'),
    path('Configuracion/Lista/Frecuencia/eliminar_frecuencia/<int:pk>/',
         EliminarFrecuenciaView.as_view(), name='eliminar_frecuencia'),
    #  Dosis
    path('Configuracion/Lista/Dosis/', ConfiguracionListDosisView.as_view(),
         name='configuracion_listado'),
    path('Configuracion/Lista/Dosis/Nuevo', CrearDosisView.as_view(), name='crear_dosis'),
    path('Configuracion/Lista/Dosis/editar_dosis/<int:pk>/', EditarDosisView.as_view(),
         name='editar_dosis'),
    path('Configuracion/Lista/Dosis/eliminar_frecuencia/<int:pk>/',
         EliminarDosisView.as_view(), name='eliminar_dosis'),

    #  Dosis
    path('Configuracion/Lista/Dosis/', ConfiguracionListDosisView.as_view(),
         name='configuracion_listado'),
    path('Configuracion/Lista/Dosis/Nuevo', CrearDosisView.as_view(), name='crear_dosis'),
    path('Configuracion/Lista/Dosis/editar_dosis/<int:pk>/', EditarDosisView.as_view(),
         name='editar_dosis'),
    path('Configuracion/Lista/Dosis/eliminar_frecuencia/<int:pk>/',
         EliminarDosisView.as_view(), name='eliminar_dosis'),

    #  Duracion
    path('Configuracion/Lista/Duracion/', ConfiguracionListDuracionView.as_view(),
         name='configuracion_listadu'),
    path('Configuracion/Lista/Duracion/Nuevo', CrearDuracionView.as_view(), name='crear_duracion'),
    path('Configuracion/Lista/Duracion/editar_duracion/<int:pk>/', EditarDuracionView.as_view(),
         name='editar_duracion'),
    path('Configuracion/Lista/Duracion/eliminar_duracion/<int:pk>/',
         EliminarDuracionView.as_view(), name='eliminar_duracion'),
    #  Sintoma
    path('Configuracion/Lista/Sintoma/', ConfiguracionListSintomaView.as_view(),
         name='configuracion_listasin'),
    path('Configuracion/Lista/Sintoma/Nuevo', CrearSintomaView.as_view(), name='crear_sintoma'),
    path('Configuracion/Lista/Sintoma/editar_sintoma/<int:pk>/', EditarSintomaView.as_view(),
         name='editar_sintoma'),
    path('Configuracion/Lista/Sintoma/eliminar_duracion/<int:pk>/',
         EliminarSintomaView.as_view(), name='eliminar_sintoma'),
    #  Diagnostico
    path('Configuracion/Lista/Diagnostico/', ConfiguracionListDiagnosticoView.as_view(),
         name='configuracion_listadia'),
    path('Configuracion/Lista/Diagnostico/Nuevo', CrearDiagnosticoView.as_view(), name='crear_diagnostico'),
    path('Configuracion/Lista/Diagnostico/editar_diagnostico/<int:pk>/', EditarDiagnosticoView.as_view(),
         name='editar_diagnostico'),
    path('Configuracion/Lista/Diagnostico/eliminar_diagnostico/<int:pk>/',
         EliminarDiagnosticoView.as_view(), name='eliminar_diagnostico'),

    #  SignoVital
    path('Configuracion/Lista/SignoVital/', ConfiguracionListSignoVitalView.as_view(),
         name='configuracion_listasv'),
    path('Configuracion/Lista/SignoVital/Nuevo', CrearSignoVitalView.as_view(), name='crear_signovital'),
    path('Configuracion/Lista/SignoVital/editar_signovital/<int:pk>/', EditarSignoVitalView.as_view(),
         name='editar_signovital'),
    path('Configuracion/Lista/SignoVital/eliminar_signovital/<int:pk>/',
         EliminarSignoVitalView.as_view(), name='eliminar_signovital'),

    #  Estudio de Gabinete
    path('Configuracion/Lista/EstudioGabinete/', ConfiguracionListEstudioGabineteView.as_view(),
         name='configuracion_listaseg'),
    path('Configuracion/Lista/EstudioGabinete/Nuevo', CrearEstudioGabineteView.as_view(), name='crear_estudiogabinete'),
    path('Configuracion/Lista/EstudioGabinete/editar_estudiogabinete/<int:pk>/', EditarEstudioGabineteView.as_view(),
         name='editar_estudiogabinete'),
    path('Configuracion/Lista/EstudioGabinete/eliminar_estudiogabinete/<int:pk>/',
         EliminarEstudioGabineteView.as_view(), name='eliminar_estudiogabinete'),

    # Agenda
    path('Agenda/', AgendaView.as_view(), name='agenda'),

    # Cita
    path('cita/', CitaView.as_view(), name='cita'),
    path('cita/editar_cita/<int:pk>/', EditarcitaView.as_view(),
         name='editar_cita'),
    path('cita/eliminar_cita/<int:pk>/', EliminarcitaView.as_view(),
         name='eliminar_cita'),




]
