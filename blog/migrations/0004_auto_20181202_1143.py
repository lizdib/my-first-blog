# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-02 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181202_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='result',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='reply_register',
            name='result',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='request',
            name='reason',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='request_register',
            name='reason',
            field=models.CharField(max_length=100),
        ),
    ]