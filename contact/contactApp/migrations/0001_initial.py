# Generated by Django 5.0.1 on 2024-07-08 19:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrimCont',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('emails', models.EmailField(blank=True, max_length=254, null=True)),
                ('phones', models.CharField(blank=True, max_length=10, null=True)),
                ('linked_id', models.IntegerField(blank=True, null=True)),
                ('link_precedence', models.CharField(choices=[('primary', 'primary'), ('secondary', 'secondary')], default='primary', max_length=10)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('DeletedAt', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SecCont',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secondary_contact_id', models.IntegerField()),
                ('cont', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondary_contacts', to='contactApp.primcont')),
            ],
        ),
    ]
