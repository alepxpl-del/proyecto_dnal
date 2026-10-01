from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Maquina, Reparacion
from .forms import MiFormularioDeCreacion
from django.contrib.auth.views import LoginView
from .forms import MaquinaForm, ReparacionForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PerfilForm

def dnal(request):
    return render(request, 'principal.html')

class ListaDeMaquinas(ListView):
    model = Maquina
    template_name = 'maquinas/lista.html'
    context_object_name = 'maquinas'   

class VerMaquina(DetailView):
    model = Maquina
    template_name = 'maquinas/detalle.html'
    context_object_name = 'maquina'

from django.contrib.auth.mixins import LoginRequiredMixin 

class AñadirMaquina(LoginRequiredMixin, CreateView):
    model = Maquina
    template_name = 'maquinas/form_add.html'
    form_class = MaquinaForm
    success_url = reverse_lazy('maquina_list')

class EditarMaquina(LoginRequiredMixin, UpdateView):
    model = Maquina
    template_name = 'maquinas/form_edit.html'
    form_class = MaquinaForm
    success_url = reverse_lazy('maquina_list')

class EliminarMaquina(LoginRequiredMixin, DeleteView):
    model = Maquina
    template_name = 'maquinas/confirm_delete.html'
    success_url = reverse_lazy('maquina_list')

class Reparaciones(LoginRequiredMixin, ListView):
    model = Reparacion
    template_name = 'reparaciones/lista.html'
    context_object_name = 'reparaciones'
    ordering = ['-fecha_ingreso']

class VerReparacion(LoginRequiredMixin, DetailView):
    model = Reparacion
    template_name = 'reparaciones/detalle.html'
    context_object_name = 'reparacion'

class AgregarReparacion(LoginRequiredMixin, CreateView):
    model = Reparacion
    template_name = 'reparaciones/form_add.html'
    form_class = ReparacionForm
    success_url = reverse_lazy('reparacion_list')

class EditarReparacion(LoginRequiredMixin, UpdateView):
    model = Reparacion
    template_name = 'reparaciones/form_add.html'
    fields = ['maquina', 'problema', 'trabajo_realizado', 'repuestos', 'costo_repuestos', 'costo_mano_obra', 'estado', 'fecha_entrega']
    success_url = reverse_lazy('reparacion_list')

class ElimninarReparacion(LoginRequiredMixin, DeleteView):
    model = Reparacion
    template_name = 'reparaciones/confirm_delete.html'
    success_url = reverse_lazy('reparacion_list')

class CustomLoginView(LoginView):
    template_name = 'registros/login.html'

class SignUpView(CreateView):
    form_class = MiFormularioDeCreacion
    template_name = 'registros/registro.html'
    success_url = reverse_lazy('login')

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Perfil actualizado con éxito!")
            return redirect('editar_perfil')
    else:
        form = PerfilForm(instance=request.user)
        
    return render(request, 'registros/perfil.html', {'form': form})