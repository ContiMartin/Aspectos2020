# Generated by Django 2.2.5 on 2019-11-06 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0004_auto_20191106_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medico',
            name='pacientes',
        ),
    ]