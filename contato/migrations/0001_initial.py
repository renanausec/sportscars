# Generated by Django 4.0.2 on 2022-02-17 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('carro_id', models.IntegerField()),
                ('customer_need', models.CharField(max_length=100)),
                ('carro_nome', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('telefone', models.CharField(max_length=100)),
                ('mensagem', models.TextField(blank=True)),
                ('user_id', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
