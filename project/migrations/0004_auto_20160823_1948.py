# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-08-24 00:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20160822_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_image',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterUniqueTogether(
            name='project_image',
            unique_together=set([('project', 'order')]),
        ),
    ]
