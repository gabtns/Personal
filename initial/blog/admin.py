from django.contrib import admin
from .models import Categorias,Post
from anaconda_navigator.widgets.manager import model
from bokeh.core.property import readonly
# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):  
    readonly_fields = ("created", "updated")
    
class PostAdmin(admin.ModelAdmin):  
    readonly_fields = ("created", "updated")
    

admin.site.register(Categorias, CategoriaAdmin)
admin.site.register(Post,PostAdmin)