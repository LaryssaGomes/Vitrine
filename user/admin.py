from django.contrib import admin
from .models import Producto
# Register your models here.
class ProjetoAdmin(admin.ModelAdmin):
    list_display = '__all__'


# Register your models here.
admin.site.register(Producto)