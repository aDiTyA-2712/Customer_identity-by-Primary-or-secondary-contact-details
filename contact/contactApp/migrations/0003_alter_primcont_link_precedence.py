# Generated by Django 5.0.1 on 2024-07-10 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0002_rename_deletedat_primcont_deletedat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primcont',
            name='link_precedence',
            field=models.CharField(choices=[('primary', 'Primary'), ('secondary', 'Secondary')], default='primary', max_length=10),
        ),
    ]