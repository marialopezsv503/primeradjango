from django.urls import path

## from myapp import views  ### Esta linea import se puede sustituir por la siguiente y como 
##    ya dentro de la carpeta "myapp" este texto se puede sustituir por el punto del siguiente import
from . import views

urlpatterns = [
    path('',views.index),  ## Se deja en blanco para que cuando se ingrese al localhost sin nada despliegue el mensaje de la funcion "HelloMundo"
    path('about/',views.about,name='about'),
    path('mitabla/',views.tablita,name='mitabla'),
    path('hello/<int:id>',views.helloMundo,name='hello'),
    path('projectmio/',views.projectmio,name='proyecto'),
    path('projectmio/<int:id>',views.project_detail,name='proyectodetalle'),
    path('tasktarea3/',views.tasktarea3,name='tasktarea3'),
    path('creaproyecto',views.create_projects,name='creaproyecto')
]