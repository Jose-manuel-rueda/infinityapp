import os
from pathlib import Path

from django.contrib.messages import constants as messages

# RUTA BASE DEL PROYECTO
BASE_DIR = Path(__file__).resolve().parent.parent

# CONFIGURACIÓN DE LA CLAVE SECRETA
SECRET_KEY = 'tu-clave-secreta-generada-por-django'

# MODO DEBUG
DEBUG = False  # Cambiar a False en producción

# HOSTS PERMITIDOS
ALLOWED_HOSTS = ['infinityapp.es', 'www.infinityapp.es']


# APLICACIONES INSTALADAS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Aplicaciones personalizadas
    'infinity_app.usuarios',  # Asegúrate de usar la ruta completa
]

# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLS Y WSGI
ROOT_URLCONF = 'infinity_app.urls'

WSGI_APPLICATION = 'infinity_app.wsgi.application'

# CONFIGURACIÓN DE BASE DE DATOS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'datos_app',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



# VALIDADORES DE CONTRASEÑAS
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# CONFIGURACIÓN DE LOCALIZACIÓN
LANGUAGE_CODE = 'es-es'  # Idioma predeterminado
TIME_ZONE = 'Europe/Madrid'  # Zona horaria
USE_I18N = True
USE_L10N = True
USE_TZ = True

# CONFIGURACIÓN DE ARCHIVOS ESTÁTICOS
STATIC_URL = '/static/'
STATIC_ROOT = '/home/usuario_cpanel/public_html/static/'
# CONFIGURACIÓN DE ARCHIVOS MEDIA (SUBIDOS POR USUARIOS)
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/usuario_cpanel/public_html/media/'
# CONFIGURACIÓN DE LA SESIÓN
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# EMAIL CONFIGURATION (si lo necesitas)
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'tu-servidor-de-correo'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'tu-usuario'
# EMAIL_HOST_PASSWORD = 'tu-contraseña'

# CONFIGURACIÓN ADICIONAL SI SE NECESITA
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Archivo settings.py

LOGIN_URL = '/usuarios/login/'
LOGIN_REDIRECT_URL = '/usuarios/perfil/'  # Esto asegura que se redirige al perfil después de iniciar sesión
LOGOUT_REDIRECT_URL = '/usuarios/login/'  # Redirige al login después de cerrar sesión
# Redirige después del inicio de sesión
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            r'C:\Users\jusep8888\Desktop\infinityapp\infinity_app\templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# Backend de correo para desarrollo (solo muestra el correo en la consola)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Configuración para un servidor SMTP (ejemplo)
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.example.com'
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True
#EMAIL_HOST_USER = 'tu_correo@example.com'
#EMAIL_HOST_PASSWORD = 'tu_contraseña'


MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

DEBUG = True

CSRF_TRUSTED_ORIGINS = [
    'https://b8ad-79-117-103-247.ngrok-free.app',  # Dominio de ngrok
]

