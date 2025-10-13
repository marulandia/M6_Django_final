import os
import django

if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "truequeapp.settings")
django.setup()

from django.contrib.auth.models import User
from productos.models import Producto

elena = User.objects.get(username="elena")
juana = User.objects.get(username="juana")

datos = [
    ("Guitarra clasica", "Buen sonido, encordado nuevo", "$80.000", "Bueno", elena),
    ("Bicicleta urbana", "Rodado 28, frenos en buen estado", "$120.000", "Uso evidente", juana),
    ("Notebook 14", "Ideal para estudio, 8GB RAM", "$250.000", "Bueno", elena),
    ("Silla gamer", "Reclinable, detalles de uso", "$90.000", "Uso evidente", juana),
    ("Auriculares", "Over-ear, cable reemplazable", "$20.000", "Como nuevo", elena),
    ("Mesa de luz", "Madera, un cajon", "$15.000", "Bueno", juana),
    ("Monitor 24", "1080p, sin pixeles muertos", "$70.000", "Como nuevo", elena),
    ("Teléfono Android", "64GB, bateria bien", "$85.000", "Bueno", juana),
    ("Impresora", "Inyección, necesita tinta", "$30.000", "Uso evidente", elena),
    ("Microfono USB", "Para streaming, buena captura", "$40.000", "Como nuevo", juana),
]

for titulo, desc, precio, estado, vendedor in datos:
    Producto.objects.get_or_create(
        titulo=titulo,
        vendedor=vendedor,
        defaults={
            "descripcion": desc,
            "precio": precio,
            "estado": estado,
        },
    )

print("10 productos cargados).")


   
#type productos/scripts/carga_productos.py | python manage.py shell