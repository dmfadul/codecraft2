# Generated by Django 5.1.6 on 2025-03-12 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poker', '0006_alter_rangeentry_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rangeentry',
            name='stack',
        ),
    ]
