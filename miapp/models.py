from email.policy import default
from importlib.resources import contents
from turtle import title, update
from venv import create
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="titulo")
    content = models.TextField(verbose_name="contenido")
    image = models.ImageField(default='null', verbose_name="miniatura", upload_to='articles'  )
    public = models.BooleanField(verbose_name="publicado")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="creado")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Editado")

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['-create_at']

    def __str__(self):

        if self.public:
            public = "(publicado)"
        else:
            public = "(privado)"

        return f"{self.title} {public}"



class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    create_at = models.DateField()

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
