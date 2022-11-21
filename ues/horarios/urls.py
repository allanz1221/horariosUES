from django.urls import path

# Create your views here.
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('aula/<int:id>', views.aula, name = 'aula'),
    path('maestro/<int:id>', views.maestro, name = 'maestro'),
    path('api/clase/aula/<int:id>', views.claseJson, name = 'claseJSON'),
    path('api/prueba/<int:id_pe>/<int:id_semestre>/<str:grupo>', views.Horario_Generacion, name = 'Horario_Generacion'),

]