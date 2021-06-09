# Generated by Django 3.1.3 on 2021-06-09 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_recepcion_pedido_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boleta',
            name='venta_id_venta',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='empleado_rut_empleado',
        ),
        migrations.AddField(
            model_name='boleta',
            name='descripcion',
            field=models.CharField(default='Descripcion', max_length=100),
        ),
        migrations.AddField(
            model_name='venta',
            name='descripcion',
            field=models.CharField(default='Descripcion', max_length=100),
        ),
    ]
