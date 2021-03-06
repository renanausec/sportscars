# Generated by Django 4.0.2 on 2022-02-14 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(max_length=255)),
                ('ultimo_nome', models.CharField(max_length=255)),
                ('cargo', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='fotos/%Y/%m/%d/')),
                ('facebook_link', models.URLField(max_length=100)),
                ('instagram_link', models.URLField(max_length=100)),
                ('linkedin_link', models.URLField(max_length=100)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
