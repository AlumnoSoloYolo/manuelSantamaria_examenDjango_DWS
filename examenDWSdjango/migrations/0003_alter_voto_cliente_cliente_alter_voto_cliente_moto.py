# Generated by Django 5.1.3 on 2024-11-05 08:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenDWSdjango', '0002_rename_estado_voto_cliente_puntuacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voto_cliente',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voto_cliente', to='examenDWSdjango.cliente'),
        ),
        migrations.AlterField(
            model_name='voto_cliente',
            name='moto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voto_moto', to='examenDWSdjango.moto'),
        ),
    ]
