# Generated by Django 4.2.3 on 2023-07-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tallerdb', '0002_boleta_producto_detalle_boleta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes', verbose_name='Imagen'),
        ),
    ]
