# Generated by Django 5.1.6 on 2025-03-12 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poker', '0005_rangeentry_stack_depth'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rangeentry',
            unique_together={('position', 'hand')},
        ),
    ]
