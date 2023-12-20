from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from bokeh.document import document

urlpatterns = [
    
    path("", views.home, name="home"),
    path("tienda/", views.tienda, name="tienda"),
    path("contactos/", views.contactos, name="contactos"),
    path("blog/", views.contactos, name="blog"),
    
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
