from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Maestro, Pe, Aula, Materia, Clase
from django.utils.timezone import localdate
from django.views.defaults import bad_request, server_error
#from .forms import AddCita
from django.contrib import messages

def index(request):
    #citas = list(Cita.objects.values())
    #return JsonResponse(citas, safe=False)
    #return HttpResponse("Hola")
    aulas = Aula.objects.all()
    context = {
        "aulas": aulas,
    }
    return render(request, "index.html", context)

def aula(request, id):
    #citas = list(Cita.objects.values())
    #return JsonResponse(citas, safe=False)
    #return HttpResponse("Hola")
    aulas = Aula.objects.filter(id=id)
    context = {
        "aulas": aulas,
    }
    return render(request, "aula.html", context)