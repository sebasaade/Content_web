from django.db import models
from django.utils import timezone

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "Gestor de About"
        verbose_name_plural = "Gestores de About"
        ordering = ['-created_date']
    
    def __str__(self):
        if self.title==None:
            return "ERROR-TITLE IS NULL"
        return self.title