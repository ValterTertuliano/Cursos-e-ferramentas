from django.shortcuts import render

# Create your views here.
def etapa1(request):
    contexto = {
        "titulo": "Primeira Etapa",
    }
    return render(request, 'global/etapas/etapa1.html', contexto)

def etapa2(request):
    contexto = {
        "titulo": "Segunda Etapa",
    }
    return render(request, 'global/etapas/etapa2.html', contexto)

def etapa3(request):
    contexto = {
        "titulo": "Terceira Etapa",
    }
    return render(request, 'global/etapas/etapa3.html', contexto)

def etapa4(request):
    contexto = {
        "titulo": "Quarta Etapa",
    }
    return render(request, 'global/etapas/etapa4.html', contexto)