# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Stakeholder(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, null=False)
    sigla = models.CharField(max_length=10, null=False)
    cadastro = models.DateTimeField(blank=False, null=False, default=datetime.now, editable=False)

    def __str__(self):
        return self.sigla

    class Meta:
        managed = False
        db_table = 'stakeholder'
        ordering = ['nome']
        verbose_name = 'Stakeholder'
        verbose_name_plural = 'Stakeholders'

class Responsavel(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150, null=False, blank=False)
    cargo = models.CharField(max_length=150, null=False, blank=False)
    stakeholder = models.ForeignKey(Stakeholder, verbose_name='Stakeholder', on_delete=models.CASCADE)
    usuario = models.OneToOneField(User, verbose_name='Usuário', on_delete=models.CASCADE)
    cadastro = models.DateTimeField(blank=False, null=False, default=datetime.now, editable=False)

    def __str__(self):
        return str(self.nome)

    class Meta:
        managed = False
        db_table = 'responsavel'
        ordering = ['stakeholder','id']
        verbose_name = 'Responsável'
        verbose_name_plural = 'Responsáveis'

class Sistema(models.Model):
    ESTAGIO_CHOICES = [
        ('Em Definição', 'Em Definição'),
        ('Em Desenvolvimento', 'Em Desenvolvimento'),
        ('Em Operação', 'Em Operação'),
        ('Descontinuado', 'Descontinuado')
    ]
    ACESSO_CHOICES = [
        ('Interno', 'Interno'),
        ('Externo', 'Externo'),
        ('Público', 'Público')
    ]

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    acesso = models.TextField(choices=ACESSO_CHOICES, default='Interno')  # This field type is a guess.
    endereco = models.CharField(max_length=1000, blank=True, null=True)
    stakeholder = models.ForeignKey(Stakeholder, verbose_name='Stakeholder', on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Responsavel, verbose_name='Responsavel', on_delete=models.CASCADE)
    estagio = models.TextField(choices=ESTAGIO_CHOICES, default='Em Definição')  # This field type is a guess.
    logo = models.ImageField(upload_to='logo/')
    cadastro = models.DateTimeField(blank=False, null=False, default=datetime.now, editable=False)

    def __str__(self):
        return self.titulo

    class Meta:
        managed = False
        db_table = 'sistema'
        ordering = ['stakeholder','titulo']
        verbose_name = 'Sistema'
        verbose_name_plural = 'Sistemas'


class Parametro(models.Model):
    id = models.AutoField(primary_key=True)
    chave = models.CharField(max_length=150, null=False, blank=False)
    valor = models.CharField(max_length=150, null=False, blank=False)
    cadastro = models.DateTimeField(blank=False, null=False, default=datetime.now, editable=False)

    def __str__(self):
        return str(self.id)+' - '+str(self.chave)

    class Meta:
        managed = False
        db_table = 'parametro'
        ordering = ['id']
        verbose_name = 'Parâmetro'
        verbose_name_plural = 'Parâmetros'

