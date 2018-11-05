from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title