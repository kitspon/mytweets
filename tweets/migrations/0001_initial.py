# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-15 11:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=160)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('country', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.User')),
            ],
        ),
    ]
