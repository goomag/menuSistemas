
# Create your views here.
from django.shortcuts import render
from sistemas.models import *

def home(request):
    #Carregamento de Parametros
    copyright = Parametro.objects.get(chave='copyright')
    cas = Parametro.objects.get(chave='CAS')
    email = Parametro.objects.get(chave='Email')
    portal = Parametro.objects.get(chave='Portal')

    listaSistema = Sistema.objects.all()

    listaStakeholders = Stakeholder.objects.all()

    return render(request,'home.html',{ 'title_sistemas' : 'Portifólio de Sistemas', 'copyright' :  copyright.valor, 'sistemas' : listaSistema, 'stakeholders' : listaStakeholders, 'cas' : cas, 'email' : email, 'portal' : portal})
