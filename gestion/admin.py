from django.contrib import admin
from .models import usuario, proyecto, tarea, etiqueta, asigancion_tarea, comentario

# Register your models here.
admin.site.register(usuario)
admin.site.register(proyecto)
admin.site.register(tarea)
admin.site.register(etiqueta)
admin.site.register(asigancion_tarea)
admin.site.register(comentario)