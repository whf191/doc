# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-25 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baishi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jiazhang',
            name='xingbie',
            field=models.CharField(blank=True, choices=[('boy', '\u7537'), ('girl', '\u5973')], default='boy', max_length=20, verbose_name='\u59d3\u522b'),
        ),
        migrations.AlterField(
            model_name='xuesheng',
            name='xingbie',
            field=models.CharField(choices=[('boy', '\u7537'), ('girl', '\u5973')], default='boy', max_length=20, verbose_name='\u6027\u522b'),
        ),
    ]
