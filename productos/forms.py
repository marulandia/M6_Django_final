from django import forms

class ProductoForm(forms.Form):
    titulo = forms.CharField(max_length=120, label="Título")
    descripcion = forms.CharField(widget=forms.Textarea, label="Descripción")
    precio = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")
    estado = forms.CharField(max_length=20, label="Estado")

class ContactoForm(forms.Form):
    mensaje = forms.CharField(
        label="Mensaje para el vendedor",
        widget=forms.Textarea(attrs={"rows": 4, "placeholder": "Hola, me interesa tu producto..."})
    )