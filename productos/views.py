from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm

from .models import Producto, Mensaje
from .forms import ProductoForm, ContactoForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    mis_productos = Producto.objects.filter(vendedor=request.user)

    mis_mensajes = (
        Mensaje.objects
        .select_related('producto', 'remitente')
        .filter(producto__vendedor=request.user)
        .order_by('-creado')
    )

    return render(request, 'home.html', {
        'productos': mis_productos,
        'mensajes': mis_mensajes,
    })

@login_required
@permission_required('productos.add_producto', raise_exception=True)
def crear(request):
    form = ProductoForm()
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            Producto.objects.create(
                titulo=form.cleaned_data['titulo'],
                descripcion=form.cleaned_data['descripcion'],
                precio=form.cleaned_data['precio'],
                estado=form.cleaned_data['estado'],
                vendedor=request.user
            )
            return redirect('home')
    return render(request, 'nuevo.html', {'formulario': form})

@login_required
@permission_required('productos.change_producto', raise_exception=True)
def editar(request, titulo):
    producto = get_object_or_404(Producto, titulo=titulo, vendedor=request.user)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto.titulo = form.cleaned_data['titulo']
            producto.descripcion = form.cleaned_data['descripcion']
            producto.precio = form.cleaned_data['precio']
            producto.estado = form.cleaned_data['estado']
            producto.save()
            return redirect('home')
    else:
        form = ProductoForm(initial={
            'titulo': producto.titulo,
            'descripcion': producto.descripcion,
            'precio': producto.precio,
            'estado': producto.estado
        })
    return render(request, 'editar.html', {'formulario': form, 'titulo': titulo})

@login_required
def detalle(request, titulo):
    producto = get_object_or_404(Producto, titulo=titulo)
    return render(request, 'detalle.html', {'producto': producto})

@login_required
@permission_required('productos.delete_producto', raise_exception=True)
def borrar(request, titulo):
    Producto.objects.filter(titulo=titulo, vendedor=request.user).delete()
    return redirect('home')

@login_required
def todas(request):
    return render(request, 'todas.html', {'productos': Producto.objects.all()})

@login_required
def contactar(request, titulo):   # si usas pk, cámbialo a (request, pk)
    producto = get_object_or_404(Producto, titulo=titulo)

    # El vendedor no se contacta a sí mismo
    if producto.vendedor == request.user:
        return redirect('detalle', titulo=producto.titulo)

    form = ContactoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        Mensaje.objects.create(
            producto=producto,
            remitente=request.user,
            contenido=form.cleaned_data['mensaje']
        )
        # Vista de confirmación simple
        return render(request, 'contacto_enviado.html', {'producto': producto})

    return render(request, 'contactar.html', {'form': form, 'producto': producto})

@login_required
def mis_mensajes(request):
    msgs = Mensaje.objects.select_related('producto','remitente')\
                          .filter(producto__vendedor=request.user)\
                          .order_by('-creado')
    return render(request, 'mis_mensajes.html', {'mensajes': msgs})