# Generated by Django 5.1.6 on 2025-03-12 19:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poker', '0003_stackdepth'),
    ]

    operations = [
        migrations.AddField(
            model_name='rangeentry',
            name='context',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='poker.context'),
        ),
    ]
