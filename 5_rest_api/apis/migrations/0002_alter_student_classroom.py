# Generated by Django 5.0.4 on 2024-07-13 00:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='classroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='apis.classroom'),
        ),
    ]
