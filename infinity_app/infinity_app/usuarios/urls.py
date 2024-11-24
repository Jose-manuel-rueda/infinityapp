from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('registro/', views.registro, name='registro'),
    path('registro/exitoso/', views.registro_exitoso, name='registro_exitoso'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar/', views.editar_perfil, name='editar_perfil'),
    path('cambiar-contrasena/', views.CustomPasswordChangeView.as_view(), name='cambiar_contrasena'),
    path('eliminar-foto/', views.eliminar_foto, name='eliminar_foto'),
    path('resetear-contrasena/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('resetear-contrasena/hecho/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('resetear-contrasena/confirmar/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('resetear-contrasena/completo/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]


