from django.db import models

class Maestro(models.Model):
    nombre = models.CharField(max_length=200)
    expediente = models.CharField(max_length=200)

class Pe(models.Model):
    nombre = models.CharField(max_length=200)
    clave = models.CharField(max_length=200)

class Aula(models.Model):
    nombre = models.CharField(max_length=200)

class Materia(models.Model):
    nombre = models.CharField(max_length=200)
    clave = models.CharField(max_length=200)
    pe = models.ForeignKey(Pe, on_delete=models.CASCADE)
    horas = models.IntegerField()
    horas_pla = models.IntegerField()
    horas_aula = models.IntegerField()

class Clase(models.Model):
    pe = models.ForeignKey(Pe, on_delete=models.CASCADE)
    maestro = models.ForeignKey(Maestro, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    hora = models.IntegerField()