# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-01 10:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_squashed_0011_auto_20181130_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='name_of_organisation',
        ),
    ]
