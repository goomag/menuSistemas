# Generated by Django 3.2b1 on 2021-03-13 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistemas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='responsavel',
            options={'managed': False, 'ordering': ['idstakeholder', 'id']},
        ),
        migrations.AlterModelOptions(
            name='sistema',
            options={'managed': False, 'ordering': ['idstakeholder', 'titulo']},
        ),
        migrations.AlterModelOptions(
            name='stakeholder',
            options={'managed': False, 'ordering': ['nome']},
        ),
    ]