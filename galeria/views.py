from django.shortcuts import render

def index(request):
    return render(request, 'galeria/index.html')

def imagem_view(request):
    return render(request, 'galeria/imagem.html') 