# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdls', '0006_auto_20160308_1354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sessionhistory',
            options={'verbose_name_plural': 'session histories'},
        ),
        migrations.RemoveField(
            model_name='file',
            name='is_removed',
        ),
        migrations.AddField(
            model_name='editor',
            name='has_repository',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='is_assigned',
            field=models.BooleanField(default=False),
        ),
    ]
