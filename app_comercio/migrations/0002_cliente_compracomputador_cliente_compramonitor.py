# Generated by Django 4.1.7 on 2023-05-05 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_comercio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='compraComputador',
            field=models.ManyToManyField(blank=True, to='app_comercio.computador'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='compraMonitor',
            field=models.ManyToManyField(blank=True, to='app_comercio.monitor'),
        ),
    ]