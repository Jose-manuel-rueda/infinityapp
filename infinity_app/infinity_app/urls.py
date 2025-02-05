from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .usuarios import views
from infinity_app import views
from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para la administración de Django
    path('usuarios/', include('infinity_app.usuarios.urls')),  # Ruta para tu aplicación 'usuarios'
    #path('', include('infinity_app.urls')),  # Redirige al archivo urls.py de infinity_app
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='infinity_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('perfil/', views.perfil, name='perfil'),  # Nueva URL para el perfil
]


# Configuración para servir archivos estáticos y media durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
