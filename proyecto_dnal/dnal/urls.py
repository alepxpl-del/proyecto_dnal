from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, SignUpView

urlpatterns = [
    path('', views.dnal, name="home"),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('registros/', SignUpView.as_view(), name='registro'),
    path('perfil/', views.editar_perfil, name='editar_perfil'),    
    path('reparaciones/', views.Reparaciones.as_view(), name='reparacion_list'),
    path('reparaciones/<int:pk>/', views.VerReparacion.as_view(), name='reparacion_detail'),
    path('reparaciones/crear/', views.AgregarReparacion.as_view(), name='reparacion_create'),
    path('reparaciones/<int:pk>/ediar/', views.EditarReparacion.as_view(), name='reparacion_update'),
    path('reparaciones/<int:pk>/eliminar/', views.ElimninarReparacion.as_view(), name='reparacion_delete'),
    
    path('maquinas/', views.ListaDeMaquinas.as_view(), name='maquina_list'),
    path('maquinas/<int:pk>/', views.VerMaquina.as_view(), name='maquina_detail'),
    path('maquinas/crear/', views.AñadirMaquina.as_view(), name='maquina_create'),
    path('maquinas/<int:pk>/editar/', views.EditarMaquina.as_view(), name='maquina_update'),
    path('maquinas/<int:pk>/eliminar/', views.EliminarMaquina.as_view(), name='maquina_delete'),
]