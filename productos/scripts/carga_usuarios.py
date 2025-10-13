import os
import django

if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "truequeapp.settings")
django.setup()

from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from productos.models import Producto

VENDEDOR = "vendedor"
COMPRADOR = "comprador"

for group_name in [VENDEDOR, COMPRADOR]:
    Group.objects.get_or_create(name=group_name)

ct = ContentType.objects.get_for_model(Producto)
perm_add    = Permission.objects.get(codename="add_producto",    content_type=ct)
perm_change = Permission.objects.get(codename="change_producto", content_type=ct)
perm_delete = Permission.objects.get(codename="delete_producto", content_type=ct)
perm_view   = Permission.objects.get(codename="view_producto",   content_type=ct)

view_all_perm, _ = Permission.objects.get_or_create(
    codename="view_all_producto",
    name="Ver todos los productos",
    content_type=ct,
)

g_vend = Group.objects.get(name=VENDEDOR)
g_vend.permissions.set([perm_view, perm_add, perm_change, perm_delete])  # puede ver/crear/modificar/eliminar

g_comp = Group.objects.get(name=COMPRADOR)
g_comp.permissions.set([perm_view])  # solo ver

usuarios = [
    ("elena", "elena123", [VENDEDOR], False, False),
    ("juana", "juana123", [VENDEDOR], False, False),
    ("mario", "mario123", [COMPRADOR], False, False),
    ("sofia", "sofia123", [COMPRADOR], False, False),
    ("tomas", "tomas123", [COMPRADOR], False, False),
]

for username, password, grupos, is_staff, is_super in usuarios:
    user, created = User.objects.get_or_create(username=username)
    if created:
        user.set_password(password)
    user.is_staff = is_staff
    user.is_superuser = is_super
    user.save()

    user.groups.clear()
    for gname in grupos:
        user.groups.add(Group.objects.get(name=gname))

print("Grupos y usuarios listos:")
print("  - Grupo vendedor => add/change/delete/view")
print("  - Grupo comprador => view (solo)")
print("  - Usuarios:", [u[0] for u in usuarios])

#type productos/scripts/carga_usuarios.py | python manage.py shell