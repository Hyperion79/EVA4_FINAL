# Generated by Django 4.2.5 on 2023-12-26 03:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_persona', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('fecha_reserva', models.DateField()),
                ('hora', models.TimeField()),
                ('cantidad_personas', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(15)])),
                ('estado', models.CharField(choices=[('RESERVADO', 'Reservado'), ('COMPLETADA', 'Completada'), ('ANULADA', 'Anulada'), ('NO_ASISTEN', 'No Asisten')], max_length=20)),
                ('observacion', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
