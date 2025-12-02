```markdown
# TruequeApp

TruequeApp es un marketplace sencillo de productos usados construido con Django. Permite a usuarios publicar productos, navegar listados y contactar a los vendedores mediante mensajes internos. El proyecto incorpora un control de permisos basado en grupos (vendedor / comprador) para restringir operaciones de creación, edición y eliminación de productos.

## Resumen de comportamiento
- Al iniciar sesión, el usuario accede a la vista "Mis productos", donde se listan únicamente las publicaciones del usuario autenticado.
- Los usuarios que pertenecen al grupo "vendedor" pueden crear, editar y eliminar sus propios productos.
- Los usuarios en el rol de "comprador" tienen permiso de solo lectura sobre los productos (ver listados y detalles).
- Existe un mecanismo de mensajería para que un usuario interesado contacte al vendedor sobre un producto (modelo Mensaje).

## Características principales
- CRUD para productos (según permisos de grupo).
- Listado de "Mis productos" para el usuario autenticado.
- Página de detalle de producto con información: título, descripción, precio, estado y vendedor.
- Sistema de mensajes para contactar sobre un producto (relaciona producto y remitente).
- Control de acceso mediante grupos y permisos Django (se usan permisos en plantillas y views).

## Modelos (resumen, según el código)
- Producto
  - Campos principales: título, descripción, precio, estado (nuevo/usado/otro), y ForeignKey al usuario vendedor.
  - Permisos asociados: add, change, delete, view (asignados al grupo vendedor).
- Mensaje
  - Relaciona: producto, remitente (usuario que escribe), posible receptor/vendedor y cuerpo del mensaje.
  - Campos típicos: asunto / cuerpo / fecha de creación / leído (según implementación).
- Usuario
  - Uso del modelo de usuario de Django (auth.User) para vendedores y compradores. Los roles se gestionan con grupos.

> Nota: Los nombres exactos de campos y rutas conviene verificarlos en los archivos `models.py` y `urls.py` si se desea documentarlos de forma más precisa.

## Permisos y configuración de grupos
El proyecto utiliza grupos de Django para diferenciar permisos:
- Grupo `vendedor`: permisos de agregar, cambiar, eliminar y ver sobre el modelo Producto.
- Grupo `comprador`: permiso de ver (lectura) sobre Producto.

Puedes crear y asignar permisos automáticamente desde una consola de Django (ejemplo):

```python
# Ejecutar en manage.py shell
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from app.models import Producto  # ajustar import según nombre de la app

content_type = ContentType.objects.get_for_model(Producto)

perm_add = Permission.objects.get(codename='add_producto', content_type=content_type)
perm_change = Permission.objects.get(codename='change_producto', content_type=content_type)
perm_delete = Permission.objects.get(codename='delete_producto', content_type=content_type)
perm_view = Permission.objects.get(codename='view_producto', content_type=content_type)

vendedor, _ = Group.objects.get_or_create(name='vendedor')
comprador, _ = Group.objects.get_or_create(name='comprador')

vendedor.permissions.set([perm_add, perm_change, perm_delete, perm_view])
comprador.permissions.set([perm_view])
```

Asigna usuarios a grupos desde el admin o desde shell:
```python
from django.contrib.auth.models import User, Group
u = User.objects.get(username='usuario1')
g = Group.objects.get(name='vendedor')
u.groups.add(g)
```

## Instalación y puesta en marcha
Pasos básicos para levantar el proyecto en desarrollo:

1. Clona el repositorio:
   git clone https://github.com/marulandia/M6_Django_final.git
2. Entra en la carpeta del proyecto y crea un entorno virtual:
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .venv\Scripts\activate      # Windows
3. Instala dependencias:
   pip install -r requirements.txt
4. Configura variables de entorno (si procede)
   - Ejemplo: SECRET_KEY, DEBUG, DATABASE_URL, etc.
5. Ejecuta migraciones:
   python manage.py migrate
6. Crea un superusuario (opcional, recomendado para acceder al admin):
   python manage.py createsuperuser
7. (Opcional) Crea los grupos `vendedor` y `comprador` y asigna permisos (ver sección Permisos).
8. Levanta el servidor:
   python manage.py runserver
9. Accede a la app en http://127.0.0.1:8000/

## Rutas y vistas (resumen)
Las vistas y plantillas principales detectadas en el proyecto proporcionan:
- Página principal / listado de productos.
- Vista "Mis productos" para el usuario autenticado.
- Detalle de producto.
- Formularios para crear/editar/eliminar producto (solo para vendedor).
- Formulario para enviar mensaje/contactar al vendedor sobre un producto.
Consulta `urls.py` y las vistas (views) para la lista completa y nombres de rutas exactos.

## Uso típico
- Regístrate e inicia sesión.
- Si eres vendedor: crea publicaciones de tus productos, edítalas y elimínalas.
- Si eres comprador: navega productos, ve detalles y contacta al vendedor mediante la función de mensajería.
- Admin: desde /admin/ gestiona usuarios, grupos y publicaciones.

## Desarrollo y pruebas
- Ejecuta pruebas (si existen) con:
  python manage.py test
- Para desarrollo local, activa DEBUG y usa bases de datos ligeras (SQLite).

## Contribuciones
- Antes de abrir PR, asegúrate de que las nuevas funcionalidades tienen tests y la documentación actualizada.
- Mantén las convenciones de Django si están configurados.



---

Si quieres, puedo:
- Ajustar el README con los nombres exactos de modelos, campos y rutas si me indicas los archivos relevantes (por ejemplo, `app/models.py`, `app/urls.py` o `project/urls.py`).
- Generar comandos específicos para crear los grupos/permisos basados en los nombres de las apps y modelos reales del proyecto.
```
