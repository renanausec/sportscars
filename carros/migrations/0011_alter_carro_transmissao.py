# Generated by Django 4.0.2 on 2022-02-15 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0010_carro_transmissao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='transmissao',
            field=models.CharField(choices=[('Automática', 'Automática'), ('Manual', 'Manual')], max_length=100),
        ),
    ]
