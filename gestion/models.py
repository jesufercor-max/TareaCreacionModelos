from django.db import models
from django.utils import timezone

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.CharField (max_length=100, unique=True)
    contrasenia = models.CharField(max_length=100)
    fecha_resgistro = models.DateTimeField(default=timezone.now)

class etiqueta (models.Model):
    nombre = models.CharField(max_length=100, unique=True)

class proyecto (models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField (max_length=100)
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    colaborador = models.ManyToManyField(usuario, related_name="proyectos_asignados")
    creador = models.ForeignKey (usuario, on_delete= models.CASCADE, null=True)
    
class tarea(models.Model):
    ESTADOS= {
        ("Pendiente", "Pendiente"),
        ("Progreso", "Progreso"),
        ("Completada", "Progreso"),
    }

    Estado = models.CharField(
        max_length=50,
        choices=ESTADOS,
        default="Pendiente",
    )

    completada = models.BooleanField(default=False)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField (max_length=100)
    prioridad = models.IntegerField (null=True)
    fecha_creacion = models.DateField()
    hora_vencimiento = models.TimeField()
    tarea = models.ForeignKey(usuario, on_delete = models.CASCADE, null=True)
    usuarios_asignados = models.ManyToManyField (usuario, related_name="usuarios_asignados")
    etiquetas_asociadas = models.ManyToManyField (etiqueta, related_name="etiquetas_asignadas")
    proyecto = models.ForeignKey (proyecto, on_delete = models.CASCADE, null=True)

class asigancion_tarea (models.Model):
    observaciones = models.TextField (max_length=100)
    fecha_asignacion = models.DateTimeField(default=timezone.now)

class comentario (models.Model):
    contenido = models.TextField (max_length=100)
    fecha_comentario = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(usuario, on_delete=models.CASCADE, null=True)
    tarea = models.ForeignKey(tarea, on_delete=models.CASCADE, null=True)

    
