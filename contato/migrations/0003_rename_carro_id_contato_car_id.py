# Generated by Django 4.0.2 on 2022-02-17 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0002_contato_create_date_alter_contato_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='carro_id',
            new_name='car_id',
        ),
    ]