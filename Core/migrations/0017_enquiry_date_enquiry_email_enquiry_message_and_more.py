# Generated by Django 4.2.4 on 2024-04-13 05:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0016_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='Date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enquiry',
            name='Email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='Message',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='Mobile',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='Product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Core.series'),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='Service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Core.application'),
        ),
    ]
