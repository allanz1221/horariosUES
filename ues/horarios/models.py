from django.db import models

class Maestro(models.Model):
    nombre = models.CharField(max_length=200)
    expediente = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre+" - "+self.expediente


class Pe(models.Model):
    nombre = models.CharField(max_length=200)
    clave = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre + " - " + self.clave

class Dia(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class Aula(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre = models.CharField(max_length=200)
    clave = models.CharField(max_length=200)
    pe = models.ForeignKey(Pe, on_delete=models.CASCADE)
    horas = models.IntegerField()
    horas_pla = models.IntegerField()
    horas_aula = models.IntegerField()
    semestre = models.IntegerField()
    plan = models.IntegerField()
    grupo = models.CharField(max_length=200)

    def __str__(self):
        return str(self.pe.clave) + " " + str(self.clave) + " " + str(self.nombre) + " Semestre " + str(self.semestre)  + " Plan " + str(self.plan) + " Grupo " + str(self.grupo)

class Clase(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='materias_rel')
    maestro = models.ForeignKey(Maestro, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    hora = models.IntegerField()
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.materia.pe.clave) + " "+str(self.materia) + str(self.maestro) + " "+ str(self.aula) + " "+ str(self.hora) + " "+ str(self.dia)


    def natural_key(self):
        return (self.maestro) + self.author.natural_key()