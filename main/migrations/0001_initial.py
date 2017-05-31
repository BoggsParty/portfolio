# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-05-21 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('content', models.TextField(blank=True, default='')),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'About',
                'verbose_name': 'About',
            },
        ),
        migrations.CreateModel(
            name='About_Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', help_text='internal title', max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
