from django.contrib import admin

# Register your models here.
from sistemas.models import *


class SistemaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'acesso', 'endereco', 'stakeholder', 'responsavel', 'estagio', 'logo')
    list_filter = ['acesso','estagio']
    search_fields = ['titulo']


admin.site.register(Sistema, SistemaAdmin)

class ResponsavelAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cargo', 'stakeholder', 'cadastro')
    list_filter = ['stakeholder']
    search_fields = ['nome']

admin.site.register(Responsavel,ResponsavelAdmin)


class StakeholderAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cadastro')
    search_fields = ['nome']


admin.site.register(Stakeholder, StakeholderAdmin)

class ParametroAdmin(admin.ModelAdmin):
    list_display = ('id', 'chave', 'valor', 'cadastro')
    search_fields = ['chave']


admin.site.register(Parametro, ParametroAdmin)