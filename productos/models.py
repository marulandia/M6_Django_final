from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20)  
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        permissions = [
            ("view_all_producto", "Ver todos los productos"),
        ]

class Mensaje(models.Model):
    producto  = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='mensajes')
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    contenido = models.TextField()
    creado    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Msg de {self.remitente.username} sobre {self.producto.titulo}"