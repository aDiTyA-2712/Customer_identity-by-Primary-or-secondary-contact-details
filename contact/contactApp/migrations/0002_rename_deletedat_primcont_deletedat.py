# Generated by Django 5.0.1 on 2024-07-09 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='primcont',
            old_name='DeletedAt',
            new_name='deletedAt',
        ),
    ]