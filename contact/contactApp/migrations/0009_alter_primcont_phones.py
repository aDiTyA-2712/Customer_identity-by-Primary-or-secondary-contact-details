# Generated by Django 5.0.1 on 2024-07-12 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0008_delete_seccont'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primcont',
            name='phones',
            field=models.CharField(blank=True, null=True),
        ),
    ]
