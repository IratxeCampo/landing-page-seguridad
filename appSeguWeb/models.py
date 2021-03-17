from django.db import models

# Create your models here.

class Grupete(models.Model):
    id_grupete = models.CharField(max_length=50)
    visitas = models.IntegerField()

    def __str__(self):
        return self.id_grupete

class LasHoras(models.Model):
    grupete = models.ForeignKey(Grupete, on_delete=models.CASCADE)
    datetime_acceso = models.DateTimeField()

    def __str__(self):
        return self.grupete.id_grupete + '_' + str(self.datetime_acceso)