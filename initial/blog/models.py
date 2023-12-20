from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Categorias(models.Model): 
    nombre = models.CharField(max_length=89) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre
    class meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    
class Post(models.Model):
    titulo = models.CharField(max_length=89)
    contenido = models.CharField(max_length=60)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)  # null= True,blank=True,
    # quiere decir que el usuario puede o no dejar en blanco estas opciones de cargar imagenes.
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categorias)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo
    class meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    
    