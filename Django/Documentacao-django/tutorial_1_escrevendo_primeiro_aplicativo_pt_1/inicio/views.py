from django.http import HttpResponse  # type: ignore
from inicio.models import Pergunta
from django.shortcuts import render, get_object_or_404 # type: ignore
from django.http import Http404


def index(request):
    lista_de_perguntas = Pergunta.objects.order_by("-data_publicacao")[:5]
    contexto = {"lista_de_perguntas": lista_de_perguntas}
    return render(request, 'inicio/index.html', contexto)


def detalhes(request, pergunta_id):

    perguntas = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, 'inicio/detalhes.html', {"perguntas": perguntas})


def resultados(request, pergunta_id):
    return HttpResponse("O resultado da pergunta: ", pergunta_id)


def votos(request, pergunta_id):
    return HttpResponse("Você esta votando para a pergunta: ", pergunta_id)
