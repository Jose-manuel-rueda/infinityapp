from django.apps import AppConfig

class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'infinity_app.usuarios'

    def ready(self):
        import infinity_app.usuarios.signals
