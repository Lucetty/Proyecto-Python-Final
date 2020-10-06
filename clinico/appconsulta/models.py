from django.db import models
from django.utils.timezone import now
from datetime import datetime, date
from appbase.models import (Paciente, Sintoma, Diagnostico,
                            EstudioGabinete, Medicamento, Dosis, Frecuencia,
                            Duracion, SignoVital, Paciente, Antecedente, GrupoAntecedente)


class Receta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    fecha = models.DateField(
        'Fecha de Atencion', blank=True, null=True, default=date.today())
    hora = models.TimeField('Hora', default=datetime.now().time())
    motivo = models.CharField('Motivo de Consulta', max_length=50)
    sintoma = models.ForeignKey(Sintoma, on_delete=models.PROTECT)
    exploracion = models.TextField('Exploracion Fisica')
    diagnostico = models.ManyToManyField(Diagnostico, null=True)
    gabinete = models.ManyToManyField(
        EstudioGabinete, null=True)
    instrucciones = models.TextField('Instrucciones Medicas')
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'

    def __str__(self):
        return '{}'.format(self.fecha)


class DetalleReceta(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.PROTECT)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.PROTECT)
    cantidad = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    dosis = models.ForeignKey(Dosis, on_delete=models.PROTECT)
    frecuencia = models.ForeignKey(Frecuencia, on_delete=models.PROTECT)
    duracion = models.ForeignKey(Duracion, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'DetalleReceta'
        verbose_name_plural = 'DetalleRecetas'

    def __str__(self):
        return '{}'.format(self.id)


class TomarSignoVital(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.PROTECT)
    signovital = models.ForeignKey(SignoVital, on_delete=models.PROTECT)
    valor = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Tomar Signo Vital'
        verbose_name_plural = 'Tomar Signo Vitales'

    def __str__(self):
        return '{}'.format(self.id)


class Historia(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    fecha = models.DateField(
        'Fecha de Historia', blank=True, null=True, default=date.today())
    hora = models.TimeField('Hora', default=datetime.now().time())
    historiaNo = models.CharField('Numero de Historia', max_length=50)
    notasinterna = models.TextField('Notas Internas')
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Historia'
        verbose_name_plural = 'Historia Clinicas'

    def __str__(self):
        return '{}'.format(self.fecha)


class HistoriaDetalle(models.Model):
    historia = models.ForeignKey(Historia, on_delete=models.PROTECT)
    GrupoAntecedente = models.ForeignKey(
        GrupoAntecedente, on_delete=models.PROTECT, null=True, blank=True)
    antecedente = models.ForeignKey(Antecedente, on_delete=models.PROTECT)
    descripcion = models.CharField('Antecedente', max_length=300)

    class Meta:
        verbose_name = 'Detalle de la Historia Clinica'
        verbose_name_plural = 'Detalle de las Historias Clinicas'

    def __str__(self):
        return '{}'.format(self.descripcion)
