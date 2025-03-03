from django.urls import path
from contatos.views import index

app_name = 'contatos'

urlpatterns = [
    path('', index, name='index'),
]
