# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-25 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('title', models.CharField(default='', max_length=200)),
                ('name_of_inhabitant', models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_organisation', models.CharField(max_length=200)),
                ('result', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('title1', models.CharField(default='', max_length=200)),
                ('name_of_inhabitant1', models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('reason', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
