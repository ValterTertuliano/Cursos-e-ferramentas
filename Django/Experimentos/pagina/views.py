from django.shortcuts import render

# Create your views here.
def paginaInicial(request):
    return render(request, 'global/pagina/inicio.html')