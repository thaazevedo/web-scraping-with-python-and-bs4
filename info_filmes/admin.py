from django.contrib import admin
from info_filmes.models import FilmesInfos
# Register your models here.


class FilmesInfosAdmin(admin.ModelAdmin):
    model = FilmesInfos
    list_display = ('titulo', 'nota', 'link_filme', 'link_poster')

admin.site.register(FilmesInfos, FilmesInfosAdmin)
