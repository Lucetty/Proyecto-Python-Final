from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


class Provincia(models.Model):
    descripcion = models.CharField(verbose_name='Descripcion', max_length=100)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

    def __str__(self):
        return '{}'.format(self.descripcion)


class Ciudad(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)
    descripcion = models.CharField(verbose_name='Descripcion', max_length=100)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return '{}'.format(self.descripcion)


class Profesion(models.Model):
    descripcion = models.CharField(
        verbose_name='Descripcion', max_length=100, unique=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Profesion'
        verbose_name_plural = 'Profesiones'

    def __str__(self):
        return '{}'.format(self.descripcion)


class Titulo(models.Model):
    descripcion = models.CharField(
        verbose_name='Descripcion', max_length=100, unique=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Titulo'
        verbose_name_plural = 'Titulos'

    def __str__(self):
        return '{}'.format(self.descripcion)


class Persona(models.Model):
    tipo_sexo = (('N', 'Ninguno'), ('M', 'Masculino'), ('F', 'Femenino'))
    estado_civil = (('S', 'Soltero'), ('C', 'Casado'),
                    ('D', 'Divorciado'), ('V', 'Viudo'), ('U', 'Union'))
    cedula = models.CharField('Cedula', max_length=13, unique=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombres')
    apellido = models.CharField(max_length=100, verbose_name='Apellidos')
    nacimiento = models.DateField('Fecha Nacimiento', blank=True, null=True)
    sexo = models.CharField('sexo', choices=tipo_sexo,
                            default='N', max_length=1)
    civil = models.CharField(
        'Estado civil', choices=estado_civil, default='S', max_length=1)
    profesion = models.ManyToManyField(Profesion)
    titulo = models.ManyToManyField(Titulo)
    provincia = models.ForeignKey(
        Provincia, on_delete=models.PROTECT, blank=True, null=True)
    ciudad = models.ForeignKey(
        Ciudad, on_delete=models.PROTECT, blank=True, null=True)
    direccion = models.CharField(
        'Direccion', max_length=100, blank=True, null=True)
    telefono = models.CharField(
        'Telefono', max_length=100, blank=True, null=True)
    email = models.EmailField('Correo', max_length=100, blank=True, null=True)
    foto = models.ImageField('Foto', upload_to='fotos/', blank=True, null=True)

    class Meta:
        abstract = True

    def get_foto(self):
        try:
            return str(self.foto.url)
        except:
            pass
        return None


class Sangre(models.Model):
    tipo = models.CharField('Tipo de Sangre', max_length=20, unique=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Tipo de Sangre'
        verbose_name_plural = 'Tipos de Sangre'

    def __str__(self):
        return '{}'.format(self.tipo)


class Horario(models.Model):
    DIA_SEMANA = ((0, 'Domingo'), (1, 'Lunes'), (2, 'Martes'),
                  (3, 'Miercoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sabado'))
    dia = models.IntegerField('Dia', choices=DIA_SEMANA, default=1)
    desde = models.TimeField('Desde', blank=True, null=True, default='00:00')
    hasta = models.TimeField('Hasta', blank=True, null=True, default='00:00')
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
        ordering = ['dia']

    def __str__(self):
        return '{} : {}'.format(self.DIA_SEMANA[self.dia][1], str(self.desde) + ' - ' + str(self.hasta))

    def dia_semana(self):
        return self.DIA_SEMANA[self.dia][1]


class Paciente(Persona):
    sangre = models.ForeignKey(
        Sangre, on_delete=models.PROTECT, blank=True, null=True)
    hijos = models.IntegerField('No.hijos', default=0)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return '{}'.format(self.nombre)


class Doctor(Persona):
    consultorio = models.CharField('Nombre de Consultorio', max_length=100)
    lugar = models.CharField('Direccion de Consultorio', max_length=100)
    logo = models.ImageField('Logo', upload_to='logos/', blank=True, null=True)
    horario = models.ManyToManyField(Horario)
    registro = models.CharField('Registro Medico', max_length=50)
    duracion = models.IntegerField('Duracion de Consulta', default=30)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctores'

    def __str__(self):
        return '{}'.format(self.nombre)


class Agenda(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    fecha = models.DateField(
        'Fecha de Agenda', blank=True, null=True)
    hora = models.TimeField('Hora')
    motivo = models.CharField('Motivo de Consulta', max_length=100)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'

    def __str__(self):
        return '{} {}'.format(self.fecha, self.hora)


class GrupoAntecedente(models.Model):
    descripcion = models.CharField(
        'Grupo de Antecedente', max_length=100, unique=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Grupo de Antecedente'
        verbose_name_plural = 'Grupo de Antecedentes'

    def __str__(self):
        return '{}'.format(self.descripcion)


class Antecedente(models.Model):
    grupoAntecedente = models.ForeignKey(
        GrupoAntecedente, on_delete=models.PROTECT)
    descripcion = models.CharField('Antecedente', max_length=100, unique=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Antecedente'
        verbose_name_plural = 'Antecedentes'

    def __str__(self):
        return '{}'.format(self.descripcion)


class Medicamento(models.Model):
    descripcion = models.CharField('Medicamento', max_length=100)
    foto = models.ImageField(
        'Foto', upload_to='medicamentos/', blank=True, null=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'

    def __str__(self):
        return '{}'.format(self.descripcion)


class Frecuencia(models.Model):
    descripcion = models.CharField('Frecuencia', max_length=100)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Frecuencia'
        verbose_name_plural = 'Frecuencias'

    def __str__(self):
        return '{}'.format(self.descripcion)


class Dosis(models.Model):
    descripcion = models.CharField('Dosis', max_length=100)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Dosis'
        verbose_name_plural = 'Dosis'

    def __str__(self):
        return '{}'.format(self.descripcion)


class Duracion(models.Model):
    descripcion = models.CharField('Duracion', max_length=100)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Duracion'
        verbose_name_plural = 'Frecuencias'

    def __str__(self):
        return '{}'.format(self.descripcion)


class Sintoma(models.Model):
    descripcion = models.CharField('Sintoma', max_length=100)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Sintoma'
        verbose_name_plural = 'Sintomas'

    def __str__(self):
        return '{}'.format(self.descripcion)


class Diagnostico(models.Model):
    codigo = models.CharField('Codigo', max_length=100)
    descripcion = models.CharField('Diagnostico', max_length=100)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Diagnostico'
        verbose_name_plural = 'Diagnosticos'

    def __str__(self):
        return '{}'.format(self.descripcion)


class SignoVital(models.Model):
    descripcion = models.CharField('Signo', max_length=100)
    rango1 = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    rango2 = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    medida = models.CharField('Medida', max_length=10)
    imagen = models.ImageField(
        'imagen', upload_to='signovital/', blank=True, null=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Signo Vital'
        verbose_name_plural = 'Signo Vitales'

    def __str__(self):
        return '{}'.format(self.descripcion)


class EstudioGabinete(models.Model):
    descripcion = models.TextField('Estudio de gabinete')
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Estudio de Gabinete'
        verbose_name_plural = 'Estudio de Gabinete'

    def __str__(self):
        return '{}'.format(self.descripcion)


class AudiUsuarioTabla(models.Model):
    TIPOS_ACCIONES = (
        ('A', 'A'),  # Adicion
        ('M', 'M'),  # Modificacion
        ('E', 'E'),  # Eliminacion
    )
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    tabla = models.CharField(max_length=100, verbose_name='Tabla')
    registroid = models.IntegerField(verbose_name='Registro Id')
    accion = models.CharField(choices=TIPOS_ACCIONES,
                              max_length=1, verbose_name='Accion')
    fecha = models.DateField(verbose_name='Fecha')
    hora = models.TimeField(verbose_name='Hora')
    estacion = models.CharField(max_length=100, verbose_name='Estacion')

    def __str__(self):
        return "{} - {} [{}]".format(self.usuario.username, self.tabla, self.accion)

    class Meta:
        verbose_name = 'Auditoria Usuario'
        verbose_name_plural = 'Auditorias Usuarios'
        ordering = ('-fecha', 'hora')
