
from django.contrib import admin
from django.urls import path,include #es necesario importar include para importar .py de urls
from django.conf import settings #importar settings.py para que tome la carpeta media


urlpatterns = [
    path('', include('core.urls')), #en lugar de importar todas las url de la app core, importo el archivo url 
    #creado en la app que contiene las urls
    path('services/', include('services.urls')),
    path('blog/', include('blog.urls')),
    path('page/', include('pages.urls')),
    path('admin/', admin.site.urls),
    
]

#para que django vaya a buscar los fichers media a la carpeta media que creamos, cuyas MEDIAURL y MEDIAROOT definimos en settings
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


