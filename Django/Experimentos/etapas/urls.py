from django.urls import path
from .  import views

app_name = 'etapas'

urlpatterns = [    
    path("1/", views.etapa1, name='etapa1'),
    path("2/", views.etapa2, name='etapa2'),
    path("3/", views.etapa3, name='etapa3'),
    path("4/", views.etapa4, name='etapa4'),

]
