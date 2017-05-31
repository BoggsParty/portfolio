# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-08-24 03:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20160823_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_image',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Categorie'),
        ),
        migrations.AddField(
            model_name='project_image',
            name='type',
            field=models.CharField(choices=[('D', 'Design'), ('B', 'Built')], default='D', max_length=1),
        ),
    ]