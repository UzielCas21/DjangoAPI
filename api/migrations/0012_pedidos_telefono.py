# Generated by Django 5.1.2 on 2024-11-04 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_pedidos_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='telefono',
            field=models.BigIntegerField(default=0),
        ),
    ]
