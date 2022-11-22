from django.db import models

class Dueno(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()

    class Meta:
        verbose_name = "Dueño"
        verbose_name_plural = "Dueños"

    def __str__(self):
        return self.nombre     

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    dueño = models.ForeignKey(Dueno, on_delete=models.CASCADE)
    edad = models.IntegerField()
    descripcion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"
    
    def __str__(self):
        return self.nombre

class Consulta(models.Model):
    nombrePaciente = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fechaAtencion = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    valor = models.IntegerField()

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"

    def __str__(self):
        return self.motivo

class Estetica(models.Model):
    nombrePaciente = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fechaAtencion = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    valor = models.IntegerField()

    class Meta:
        verbose_name = "Estetica"
        verbose_name_plural = "Esteticas"

    def __str__(self):
        return self.motivo

class Vacuna(models.Model):
    nombrePaciente = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fechaAtencion = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    valor = models.IntegerField()

    class Meta:
        verbose_name = "Vacuna"
        verbose_name_plural = "Vacunas"

    def __str__(self):
        return self.motivo

class Cirugia(models.Model):
    nombrePaciente = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fechaAtencion = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    valor = models.IntegerField()

    class Meta:
        verbose_name = "Cirugia"
        verbose_name_plural = "Cirugias"

    def __str__(self):
        return self.motivo 