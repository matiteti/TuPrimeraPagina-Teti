# Generated by Django 4.2.3 on 2023-08-13 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_rename_canidad_compra_cantidad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compra',
            old_name='producto',
            new_name='fruta',
        ),
    ]
