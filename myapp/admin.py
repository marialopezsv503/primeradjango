from django.contrib import admin

# Register your models here.
## Cambios hechos para que aparezcan en el Panel-Admin de DJango

from .models import ProjectMio, TaskTarea3

admin.site.register(ProjectMio) 
admin.site.register(TaskTarea3)