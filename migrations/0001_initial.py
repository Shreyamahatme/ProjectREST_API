# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=models.CASCADE, related_name='clients_created', to=django.contrib.auth.models.User)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=models.CASCADE, related_name='projects_created', to=django.contrib.auth.models.User)),
                ('client', models.ForeignKey(on_delete=models.CASCADE, related_name='projects', to='myapp.Client')),
                ('users', models.ManyToManyField(related_name='projects', to=django.contrib.auth.models.User)),
            ],
        ),
    ]
