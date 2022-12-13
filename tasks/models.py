from django.db import models


# Create your models here.

class Status(models.TextChoices):
    UNSTARTED = 'u', "Tareas no iniciadas"
    ONGOING = 'o', "En Curso"
    FINISHED = 'f', "Finalizada"


class Task(models.Model):
    name = models.CharField(verbose_name="Nombre de la Tarea", max_length=65, unique=True)
    status = models.CharField(verbose_name="Estado de la Tarea", max_length=1, choices=Status.choices)

    def __str__(self):
        return self.name
