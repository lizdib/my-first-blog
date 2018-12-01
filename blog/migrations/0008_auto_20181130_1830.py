# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-30 15:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20181130_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply_register',
            name='name_of_inhabitant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Reply'),
        ),
        migrations.AlterField(
            model_name='request_register',
            name='name_of_inhabitant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Request'),
        ),
    ]