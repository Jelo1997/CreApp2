# Generated by Django 5.0.2 on 2024-02-22 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crea', '0013_propiedad_disponible_foto_propiedad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad_disponible',
            name='foto_propiedad',
            field=models.FileField(blank=True, upload_to='foto_propiedad_disponible/'),
        ),
    ]
