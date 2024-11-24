from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth.views import LoginView,PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EditarPerfilForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Perfil
from django.contrib.auth import login
from django.db import IntegrityError
from django.shortcuts import render





class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()  # Crea el usuario
            try:
                # Verifica si el perfil ya existe antes de crearlo
                Perfil.objects.get(user=user)
            except Perfil.DoesNotExist:
                # Si no existe, crea el perfil
                Perfil.objects.create(user=user)
                
            login(request, user)  # Inicia sesión al usuario recién registrado
            return redirect('perfil')  # Redirige al perfil después de registrarse
    else:
        form = RegistroForm()

    return render(request, 'usuarios/registro.html', {'form': form})
from django.shortcuts import render

def registro_exitoso(request):
    return render(request, 'usuarios/registro_exitoso.html')

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html', {'usuario': request.user})



@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=request.user.perfil)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado con éxito.')
            return redirect('perfil')
        else:
            messages.error(request, 'Por favor, corrija los errores a continuación.')
    else:
        form = EditarPerfilForm(instance=request.user.perfil)
    return render(request, 'usuarios/editar_perfil.html', {'form': form})
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'usuarios/cambiar_contrasena.html'
    success_url = reverse_lazy('perfil')

@login_required
def eliminar_foto(request):
    perfil = request.user.perfil
    if perfil.foto:
        perfil.foto.delete()
        perfil.save()
        messages.success(request, "La foto de perfil ha sido eliminada.")
    return redirect('perfil')    

class CustomPasswordResetView(PasswordResetView):
    template_name = 'usuarios/resetear_contrasena.html'
    email_template_name = 'usuarios/resetear_contrasena_email.html'
    subject_template_name = 'usuarios/resetear_contrasena_asunto.txt'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'usuarios/resetear_contrasena_hecho.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'usuarios/resetear_contrasena_confirmar.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'usuarios/resetear_contrasena_completo.html'

