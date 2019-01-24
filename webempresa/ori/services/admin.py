from django.contrib import admin
from .models import services #importamo el modelo para el administrador

# Register your models here.

#creamo serviceadmin 
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields= ('created','updated')

admin.site.register(services,ServiceAdmin)