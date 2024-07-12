# Generated by Django 5.0.1 on 2024-07-12 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0009_alter_primcont_phones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primcont',
            name='emails',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='primcont',
            name='link_precedence',
            field=models.CharField(choices=[('primary', 'Primary'), ('secondary', 'Secondary')], default='primary'),
        ),
    ]