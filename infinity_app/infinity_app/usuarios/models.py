from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Perfil'
    
def clean(self):
    if self.foto:
        if self.foto.size > 2 * 1024 * 1024:  # 2 MB
            raise ValidationError("La imagen no puede superar los 2 MB.")
        if not self.foto.name.lower().endswith(('.jpg', '.jpeg', '.png')):
            raise ValidationError("Formato de imagen no soportado. Usa JPG, JPEG o PNG.")
    

@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_perfil(sender, instance, **kwargs):
    instance.perfil.save()


