from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('registor',views.registor,name="registor"),
    path('login',views.login,name="login") ,
    path('logout',views.logout,name="logout")
    
    
]