from django.db import models
from anaconda_project import verbose

# Create your models here.

class servicios(models.Model):
    titulo = models.CharField(max_length=89)
    contenido = models.CharField(max_length=60)
    imagen = models.ImageField(upload_to='servicios')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo
    class meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
    
    




