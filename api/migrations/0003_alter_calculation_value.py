# Generated by Django 3.2.9 on 2021-12-21 20:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_calculation_operation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculation',
            name='value',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(max_length=255), size=None),
        ),
    ]