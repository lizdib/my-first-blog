# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-29 20:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181129_2309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='name_of_inhabitant1',
            new_name='name_of_inhabitant',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='title1',
            new_name='title',
        ),
    ]