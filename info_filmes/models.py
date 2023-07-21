from django.db import models

# Create your models here.
class FilmesInfos(models.Model):

    titulo = models.CharField(max_length=100)
    link_filme = models.TextField()
    link_poster = models.TextField()
    nota = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo
