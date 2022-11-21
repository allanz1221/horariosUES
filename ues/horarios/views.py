from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Maestro, Pe, Aula, Materia, Clase, Act_docente
from django.utils.timezone import localdate
from django.views.defaults import bad_request, server_error
#from .forms import AddCita
from django.contrib import messages

def index(request):
    #citas = list(Cita.objects.values())
    #return JsonResponse(citas, safe=False)
    #return HttpResponse("Hola")
    aulas = Aula.objects.all()
    maestros = Maestro.objects.all()
    context = {
        "aulas": aulas,
        "maestros": maestros,
    }
    return render(request, "index.html", context)

def aula(request, id):
    aulas = Aula.objects.filter(id=id)
    clases = Clase.objects.filter(aula_id=id)
    context = {
        "aulas": aulas,
        "clases": clases,
    }
    return render(request, "aula.html", context)

def maestro(request, id):
    maestros = Maestro.objects.filter(id=id)
    clases = Clase.objects.all()
    act_docentes = Act_docente.objects.filter(maestro_id=id)
    context = {
        "maestros": maestros,
        "clases": clases,
        "act_docentes": act_docentes,
    }
    return render(request, "maestro.html", context)

def claseJson(request, id):
    clases = list(Clase.objects.filter(aula_id=id).values())


    return JsonResponse(clases, safe=False)

def Horario_Generacion(request, id_pe, id_semestre, grupo):
    #http://127.0.0.1:8000/api/prueba/1/2/01
    clases = list(Clase.objects.filter(materia__semestre=id_semestre, materia__grupo=grupo, materia__pe_id=id_pe).values())
    return JsonResponse(clases, safe=False)

def guardarClase(request):
    #revisar que regrese cero en Clase Filter(id_aula, hora y dia) return aula ocupada sino despues revisar prefesor Filter (hora y dia del profesor) regresar ok o profe ocupado
    return True