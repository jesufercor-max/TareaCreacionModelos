from django.core.management.base import BaseCommand
from faker import Faker
from gestion.models import *

class Command(BaseCommand):
    help ='Generando datos usando Faker'

    def handle (self, *args, **kwargs):
        fake = Faker('es_ES')

        for _ in range(30):
            usuario.objects.create(
                nombre = fake.name(),
                correo_electronico= fake.unique.email(),
                contrasenia= fake.password (length=10),
            )
            
        self.stdout.write(self.style.SUCCESS('Datos generados correctamente'))