# Generated by Django 3.1.3 on 2021-06-03 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20210531_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='contraseña_empleado',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='nombre_usuario',
        ),
        migrations.AlterField(
            model_name='cliente_fiado',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]