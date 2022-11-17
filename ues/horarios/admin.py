from django.contrib import admin

# Register your models here.
from . models import  Maestro, Pe, Aula, Materia, Clase
admin.site.site_header = "Sitio web de Registro de Fisiterapias"
admin.site.site_title = "Universidad Estatal de Sonora"
admin.site.index_title = "Bienvenidos al portal de administración"

class MaestroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'expediente')
    use_bulk = True

admin.site.register(Maestro)

class PeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'clave')
    use_bulk = True

admin.site.register(Pe)

class AulaAdmin(admin.ModelAdmin):
    list_display = ('nombre')
    use_bulk = True

admin.site.register(Aula)


class MateriaAdmin(admin.ModelAdmin):
    #list_display = ('nombre', 'clave','pe','horas','horas_pla','horas_aula')
    list_display = ('nombre')
    use_bulk = True

admin.site.register(Materia)


class ClaseAdmin(admin.ModelAdmin):
    #list_display = ('pe', 'maestro','aula','hora')
    list_display = ('id')
    use_bulk = True

admin.site.register(Clase)