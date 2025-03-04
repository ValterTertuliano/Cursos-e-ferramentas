from django.shortcuts import render

# Create your views here.
def etapa1(request):
    return render(request, 'global/etapas/etapa1.html')

def etapa2(request):
    return render(request, 'global/etapas/etapa2.html')

def etapa3(request):
    return render(request, 'global/etapas/etapa3.html')