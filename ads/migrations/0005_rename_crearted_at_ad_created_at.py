# Generated by Django 4.0.7 on 2023-03-15 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_rename_update_at_ad_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='crearted_at',
            new_name='created_at',
        ),
    ]
