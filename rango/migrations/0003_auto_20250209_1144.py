# Generated by Django 2.2.28 on 2025-02-09 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20250209_0126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='like',
            new_name='likes',
        ),
    ]
