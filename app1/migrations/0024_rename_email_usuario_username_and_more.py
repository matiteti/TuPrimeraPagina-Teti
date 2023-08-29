# Generated by Django 4.2.3 on 2023-08-29 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0023_alter_usuario_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='email',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='last_login',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]