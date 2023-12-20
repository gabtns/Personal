from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from bokeh.document import document
from django.urls import path

urlpatterns = [
    
    path("blog/", views.blog, name="blog"),
   
    
]