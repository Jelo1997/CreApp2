# Generated by Django 5.0.2 on 2024-02-15 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crea', '0003_propiedad_disponible_id_cliente_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad_posible',
            name='es_activo',
            field=models.BooleanField(default=True, verbose_name='¿Propiedad activa?'),
        ),
    ]
