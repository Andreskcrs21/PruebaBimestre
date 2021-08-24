# Generated by Django 3.2.6 on 2021-08-24 14:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioEquipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario', models.CharField(max_length=100)),
                ('Nombres', models.CharField(max_length=100)),
                ('Apellidos', models.CharField(max_length=100)),
                ('Correo', models.CharField(max_length=100)),
                ('Equipo_Nombre', models.CharField(max_length=100)),
                ('Diagnostico', models.CharField(max_length=500)),
                ('FechaIngreso', models.DateTimeField(default=datetime.datetime(2021, 8, 24, 9, 8, 4, 255461), verbose_name='Fecha de Ingreso')),
            ],
        ),
    ]
