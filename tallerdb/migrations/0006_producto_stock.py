# Generated by Django 4.2.3 on 2023-07-13 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tallerdb', '0005_delete_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(blank=True, null=True, verbose_name='stock'),
        ),
    ]
