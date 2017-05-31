# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-08-22 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20160821_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_image',
            name='main_image',
        ),
        migrations.RemoveField(
            model_name='project_image',
            name='secondary_image',
        ),
        migrations.AddField(
            model_name='project_image',
            name='order',
            field=models.PositiveIntegerField(default=500, help_text='Order displayed. 1 is maing image'),
        ),
    ]
