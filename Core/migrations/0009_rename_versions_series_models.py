# Generated by Django 4.2.4 on 2024-04-11 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0008_series_date_series_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='series',
            old_name='Versions',
            new_name='Models',
        ),
    ]
