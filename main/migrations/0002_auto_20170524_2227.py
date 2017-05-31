# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-05-25 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_title', models.CharField(default='', max_length=200)),
                ('file', models.FileField(help_text='Uses most recent', upload_to='resume/%y/%m/%d/')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('content', models.TextField(default='')),
                ('active', models.BooleanField(default=False)),
                ('order', models.PositiveSmallIntegerField(default=1, help_text='Use this to order the sections')),
            ],
        ),
        migrations.AlterModelOptions(
            name='about_images',
            options={'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
    ]
