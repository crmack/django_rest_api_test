# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('matcher', models.CharField(choices=[('matcher1', 'Matcher1'), ('matcher2', 'Matcher2')], max_length=10)),
            ],
        ),
    ]
