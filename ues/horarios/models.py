from django.db import models

class TipoContrato(models.Model):
    nombre = models.CharField(max_length=200)
    clave = models.CharField(max_length=200)


    def __str__(self):
        return self.nombre


class Tratamiento(models.Model):
    nombre = models.CharField(max_length=200)
    clave = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    clave = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Comision(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Pe(models.Model):
    nombre = models.CharField(max_length=200)
    clave = models.CharField(max_length=200)
    nombre_jc = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre + " - " + self.clave


class Maestro(models.Model):
    nombre = models.CharField(max_length=200)
    expediente = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    pe = models.ForeignKey(Pe, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    comision = models.ForeignKey(Comision, on_delete=models.CASCADE)
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    tipocontrato = models.ForeignKey(TipoContrato, on_delete=models.CASCADE)
    contrato_inicio = models.DateField()
    contrato_fin = models.DateField()

    def __str__(self):
        return self.nombre+" - "+self.expediente



class Dia(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    nombre = models.CharField(max_length=200)
    clave = models.CharField(max_length=200)

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
    visible = models.BooleanField(default=True)
    def __str__(self):
        return str(self.materia) + str(self.maestro) + " "+ str(self.aula) + " "+ str(self.hora) + " "+ str(self.dia)


    def natural_key(self):
        return (self.maestro) + self.author.natural_key()



class Act_docente(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    maestro = models.ForeignKey(Maestro, on_delete=models.CASCADE)
    hora = models.IntegerField()
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.maestro.nombre) +" " + str(self.actividad.nombre) +" "+ str(self.dia) + " "+ str(self.hora)   