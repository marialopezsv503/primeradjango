from django.http import HttpResponse, JsonResponse  ## Se agrega JSonResponse para poder manejar el QuerySet que se trae del modelo (osea la BD SQLite)
from django.shortcuts import render, get_object_or_404,redirect
from .models import ProjectMio,TaskTarea3
from .forms import createnewproject


def index(request):
    titulito="Bienvenido amiguito a DJango"
    return render(request,"index.html",{"mititulito":titulito})  ## Se pasa la variable desde la vista hasta el template "index.html" y pasa con forma de variable diccionario

def helloMundo(request,id):
    print(type(id))
    return HttpResponse("<font size='7' color='green'> Hola Mundito %i</font>" %id)

def about(request):    
    return HttpResponse("<marquee>'About', aqui va el mensaje de AcercaDe </marquee>")

def tablita(request):
    todosprojects=ProjectMio.objects.all()
    mivariable=[2,"netillo",True,6,"Sarita"]
    return render(request,"mitemplate.html",{'mivariable':mivariable, 'todosprojects': todosprojects})


def projectmio(request):  
    ## el sig. comando se tuvo que convertir a tipo lista con la funcion "list"
    ##   además en lugar de usar objects.all()  para quitar el error se uso object.values()
    ''' varprojectmio=list(ProjectMio.objects.values())
    ## Se utilizó "JSonResponse" en lugar de "HttpResponse" porque se imprima un QuerySet (conjunto de datos)
    return JsonResponse(varprojectmio,safe=False)    '''
    #return JsonResponse(str(varprojectmio[3]) +  " <br><br> item4:" + str(varprojectmio[4]),safe=False)

    todosprojects=ProjectMio.objects.all()
    return render(request,"projects.html",{'todosprojects':todosprojects})


def tasktarea3(request):
    #t ask_variable=TaskTarea3.objects.get(id=idtask)
    
    ## para que cuando se digite un código que NO existe en la BD arroje un error, se llamara a
    ##   la funcion "get_object_or_404", se sustituyo la linea de código anterior por la siguiente
    ''' task_variable=get_object_or_404(TaskTarea3,id=idtask)
    return HttpResponse("task_variable: %s " % task_variable.title1) '''
    todastasks=TaskTarea3.objects.all()
    return render(request,"tasks.html",{'todastasks':todastasks})

def create_projects(request):
    if request.method=='GET':
        return render(request,"create_projects.html",{'form':createnewproject})
    else:
        ## print (request.POST)   # se ocupo para validar en la consola
        var_project=ProjectMio.objects.create(name=request.POST["name"])
        return redirect('proyecto')
        #print(var_project)
        #return render(request,"create_projects.html",{'form':createnewproject})
    
def project_detail(request, id):
    detproyecto=ProjectMio.objects.get(id=id)
    print ("el id es:", detproyecto)
    return render(request,'detail.html',{'datoproyecto':detproyecto})
    
     