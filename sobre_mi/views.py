from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def miPrimerHolaMundo(request):
    return HttpResponse("<span>Hola Mundo</span>")


def holaMundoHTML(request):
    titulo = "Primera página con Django"
    desarrollador = "Jorge"
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    esAdmin = False
    return render(request, 'index.html', {
        'tituloPrueba': titulo,
        'desarrollador': desarrollador,
        'numeros': lista,
        'admin': esAdmin
    })
