from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('',views.index, name="index"),
      path('index.html',views.index, name="index"),
    path('contact.html',views.contact,name="contact"),
    path('destinations.html',views.des,name="destinations"),
    
]