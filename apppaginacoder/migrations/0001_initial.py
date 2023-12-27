# Generated by Django 5.0 on 2023-12-27 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('dni', models.IntegerField(verbose_name='Dni(Sín puntos)')),
                ('cursando', models.CharField(max_length=50, verbose_name='Cursando')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('fecha_comienzo', models.DateField(verbose_name='Fecha de ingreso')),
                ('dni', models.IntegerField(verbose_name='Dni(Sín puntos)')),
                ('profe_de', models.CharField(max_length=50, verbose_name='Profesor de')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
    ]
