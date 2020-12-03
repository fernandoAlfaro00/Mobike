# Generated by Django 3.0.3 on 2020-12-03 06:30

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
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=18)),
                ('fecha_nac', models.DateField()),
                ('tarjeta', models.CharField(max_length=35)),
                ('domicilio', models.CharField(max_length=31)),
                ('comuna', models.CharField(choices=[('RE', 'Comuna la reina'), ('PRO', 'Comuna providencia'), ('FL', 'Comuna la florida')], max_length=31)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=10)),
                ('tipo_relacion', models.CharField(choices=[('T', 'Trabaja'), ('V', 'Vive')], max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
    ]
