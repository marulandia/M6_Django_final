from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout_view, name='logout'),
    path('producto/crear/', views.crear, name='crear'),
    path('producto/editar/<str:titulo>/', views.editar, name='editar'),
    path('producto/detalle/<str:titulo>/', views.detalle, name='detalle'),
    path('producto/borrar/<str:titulo>/', views.borrar, name='borrar'),
    path('producto/todas/', views.todas, name='todas'),
    path('producto/contactar/<str:titulo>/', views.contactar, name='contactar'),
    path('mensajes/', views.mis_mensajes, name='mis_mensajes'),
]


