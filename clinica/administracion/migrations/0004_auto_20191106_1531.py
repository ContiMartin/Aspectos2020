# Generated by Django 2.2.5 on 2019-11-06 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_remove_medico_apellido'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='matricula',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='medico',
            name='pacientes',
            field=models.ManyToManyField(to='administracion.Paciente'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='dni',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='edad',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='obra_social',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='medico',
            name='especialidad',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.CreateModel(
            name='HistoriaMedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='historias_medicas', to='administracion.Medico')),
                ('paciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='historias_medicas', to='administracion.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleHistoriaMedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('historia_medica', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='administracion.HistoriaMedica')),
            ],
        ),
    ]
