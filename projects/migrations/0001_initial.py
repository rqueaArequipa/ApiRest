# Generated by Django 4.1.3 on 2022-11-27 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distritos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('imagen', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('cantidad', models.IntegerField()),
                ('imagen', models.CharField(max_length=250, null=True)),
                ('distrito_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.distritos')),
            ],
        ),
        migrations.CreateModel(
            name='Jornadas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.CharField(max_length=200)),
                ('final', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Paraderos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('imagen', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rutas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('inicio', models.CharField(max_length=200)),
                ('final', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('paraderos_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.paraderos')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('rol', models.IntegerField(default=1)),
                ('password', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('distritos_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.distritos')),
            ],
        ),
        migrations.CreateModel(
            name='Unidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conductor', models.CharField(max_length=200)),
                ('placa', models.CharField(max_length=200)),
                ('longitud', models.CharField(max_length=200)),
                ('capacidad', models.IntegerField()),
                ('lapso_tiempo', models.CharField(max_length=200)),
                ('distrito_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.distritos')),
                ('empresas_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.empresas')),
                ('jornadas_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.jornadas')),
                ('rutas_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.rutas')),
            ],
        ),
        migrations.CreateModel(
            name='Rutas2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('inicio', models.CharField(max_length=200)),
                ('final', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=500)),
                ('distritos_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.distritos')),
                ('paraderos_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.paraderos')),
            ],
        ),
        migrations.AddField(
            model_name='empresas',
            name='rutas_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.rutas'),
        ),
    ]
