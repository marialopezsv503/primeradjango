from django.db import models

# Crendo mi propio modelo para crear tablas

class ProjectMio(models.Model):
    name=models.CharField(max_length=200)
    ## Se crea esta funcion para desplegar el título del proyecto en el Panel-Admin
    def __str__(self):
        return self.name

    

class TaskTarea3(models.Model):
    title1=models.CharField(max_length=200)
    description1=models.TextField()
    project=models.ForeignKey(ProjectMio, on_delete=models.CASCADE)
    done=models.BooleanField(default=False)

    def __str__(self):
        return self.title1 + ' - ' + self.project.name