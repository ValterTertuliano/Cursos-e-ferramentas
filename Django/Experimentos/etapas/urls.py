from django.urls import path
from .  import views


urlpatterns = [    
    path("1/", views.etapa1),
    path("2/", views.etapa2),
    path("3/", views.etapa3),

]
