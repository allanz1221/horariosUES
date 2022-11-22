from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from . models import  Maestro, Pe, Aula, Materia, Clase, Dia, Categoria, Tratamiento, Comision, Actividad, Act_docente, TipoContrato, Grupo, Generacion, Semestre, Plan
admin.site.site_header = "Sitio web de Horarios"
admin.site.site_title = "Universidad Estatal de Sonora"
admin.site.index_title = "Bienvenidos al portal de administración"

class MaestroResource(resources.ModelResource):
    class Meta:
        model = Maestro

class MaestroAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields= ('nombre', 'expediente', 'pe', 'categoria')
    list_display = ('nombre', 'expediente', 'pe', 'categoria')
    resource_class = MaestroResource

admin.site.register(Maestro, MaestroAdmin)

class PeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'clave')
    use_bulk = True

admin.site.register(Pe)

class AulaResource(resources.ModelResource):
    class Meta:
        model = Aula

class AulaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = AulaResource  

admin.site.register(Aula, AulaAdmin)

class MateriaResource(resources.ModelResource):
    class Meta:
        model = Materia

class MateriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    #list_display = ('nombre', 'clave','pe','horas','horas_pla','horas_aula')
    search_fields= ('nombre','clave','horas','generacion','plan')
    list_display = ('nombre','clave','horas','generacion','plan')
    use_bulk = True
    resource_class = MateriaResource


admin.site.register(Materia, MateriaAdmin)


class ClaseAdmin(admin.ModelAdmin):
    #list_display = ('pe', 'maestro','aula','hora')
    list_display = ('id')
    use_bulk = True

admin.site.register(Clase)

class DiaAdmin(admin.ModelAdmin):
    #list_display = ('pe', 'maestro','aula','hora')
    list_display = ('id')
    use_bulk = True

admin.site.register(Dia)

admin.site.register(Categoria)
admin.site.register(Tratamiento)
admin.site.register(Comision)
admin.site.register(Actividad)
admin.site.register(TipoContrato)

admin.site.register(Act_docente)
admin.site.register(Grupo)
admin.site.register(Generacion)
admin.site.register(Semestre)
admin.site.register(Plan)