from django.shortcuts import render
from django.http import HttpResponse
from .models import Evento, EventoCientifico, Pessoa, PessoaFisica, PessoaJuridica, Autor, ArtigoCientifico, ArtigoAutor, Inscricoes, TipoInscricao


def listaEvento(request):
    retorno = "<h1>Eventos</h1>"
    lista = Evento.objects.all()
    for evento in lista:
        retorno += '</br>Nome do Evento: {}</br>.format(evento.nome)'
    return HttpResponse(retorno)
