# Generated by Django 3.2b1 on 2021-03-13 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('cargo', models.CharField(max_length=150)),
                ('idstakeholder', models.BigIntegerField()),
                ('cadastro', models.DateTimeField()),
            ],
            options={
                'db_table': 'responsavel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=150)),
                ('acesso', models.TextField()),
                ('endereco', models.CharField(blank=True, max_length=1000, null=True)),
                ('idstakeholder', models.BigIntegerField(blank=True, null=True)),
                ('idresponsavel', models.BigIntegerField(blank=True, null=True)),
                ('estagio', models.TextField(blank=True, null=True)),
                ('cadastro', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sistema',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stakeholder',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('idstakeholder', models.BigIntegerField(blank=True, null=True)),
                ('cadastro', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'stakeholder',
                'managed': False,
            },
        ),
    ]
