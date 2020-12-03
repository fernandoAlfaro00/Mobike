# Generated by Django 3.0.3 on 2020-12-02 21:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_bicicleta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bicicleta',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='bicicleta',
            name='fecha_inicio',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='bicicleta',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
