# Generated by Django 4.2.2 on 2023-06-27 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('celular', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('en ruta', 'En Ruta'), ('entregado', 'Entregado'), ('cancelado', 'Cancelado')], max_length=20)),
                ('pagado', models.BooleanField(default=False)),
                ('regla_envio', models.CharField(choices=[('domicilio', 'Domicilio'), ('recoge', 'Recoge en punto')], max_length=10)),
                ('observaciones', models.TextField(blank=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.cliente')),
                ('productos', models.ManyToManyField(through='projects.DetallePedido', to='projects.producto')),
            ],
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.pedido'),
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.producto'),
        ),
    ]
