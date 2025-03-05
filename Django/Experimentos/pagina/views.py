from django.shortcuts import render

# Create your views here.
def paginaInicial(request):
    contexto = {
        "titulo": "Mapa da Página",
    }
    return render(request, 'global/pagina/inicio.html', contexto)