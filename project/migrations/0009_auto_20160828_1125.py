# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-08-28 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_project_detail_main_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_detail',
            name='summary',
        ),
        migrations.AddField(
            model_name='project_detail',
            name='duration',
            field=models.CharField(default='', help_text='Length of project', max_length=200),
        ),
    ]
