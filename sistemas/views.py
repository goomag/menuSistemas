from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from sistemas.models import *

def home(request):
    copyright = Parametro.objects.get(chave='copyright')

    listaSistema = Sistema.objects.all()

    return render(request,'home.html',{ 'title_sistemas' : 'Portifólio de Sistemas', 'copyright' :  copyright.valor, 'sistemas' : listaSistema})