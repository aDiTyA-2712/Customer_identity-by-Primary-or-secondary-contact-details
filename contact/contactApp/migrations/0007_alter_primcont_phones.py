# Generated by Django 5.0.1 on 2024-07-10 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0006_alter_primcont_link_precedence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primcont',
            name='phones',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]