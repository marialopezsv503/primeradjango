"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  ### se importa include para poder traer las URLs "myapp.urls"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls'))  ## En este "path" va vacia la primera cadena, 
      ## para que no se tenga que escribir nada en la URL que preceden a las rutas importadas
      ## ya de lo contrario, si pone por ejemplo 'casa/', esto se convertiria en prefija que tendría que llevar todas las rutas
      ## se esta incluyendo "myapp/urls.py" en el urls.py del proyecto principal y haciendo un enlace con esa app.
]
