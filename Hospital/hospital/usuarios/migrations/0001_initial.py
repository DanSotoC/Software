# Generated by Django 2.2.4 on 2020-03-05 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=20)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=15)),
                ('comuna', models.CharField(max_length=20)),
                ('domicilio', models.CharField(max_length=50)),
                ('num_domicilio', models.CharField(max_length=50)),
                ('f_nacimiento', models.CharField(max_length=20)),
                ('id_perfil', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=15)),
                ('especialidad', models.CharField(max_length=20)),
                ('file', models.FileField(upload_to='archivos/personal')),
                ('id_perfil', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido1', models.CharField(max_length=30)),
                ('apellido2', models.CharField(max_length=30)),
                ('rut', models.CharField(max_length=15)),
                ('comuna', models.CharField(max_length=20)),
                ('domicilio', models.CharField(max_length=50)),
                ('num_domicilio', models.CharField(max_length=50)),
                ('f_nacimiento', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=100)),
                ('activo', models.IntegerField(default=1)),
                ('id_tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Tutor')),
            ],
        ),
    ]