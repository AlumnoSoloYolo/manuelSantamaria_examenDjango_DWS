# Generated by Django 5.1.3 on 2024-11-05 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenDWSdjango', '0006_rename_fecha_hora_voto_cliente_fecha_voto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voto_cliente',
            name='puntuacion',
            field=models.FloatField(),
        ),
    ]
