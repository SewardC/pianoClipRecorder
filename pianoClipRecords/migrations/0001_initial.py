# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-25 22:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clip_name', models.CharField(max_length=50)),
                ('key_flow', models.CharField(max_length=250)),
                ('key_respective_space', models.CharField(max_length=250)),
                ('key_used', models.CharField(max_length=30)),
                ('key_frequency', models.CharField(max_length=30)),
                ('is_favorite', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
