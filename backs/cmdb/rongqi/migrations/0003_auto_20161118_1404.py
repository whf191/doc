# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-18 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rongqi', '0002_create_rongqi'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='create_rongqi',
            options={'verbose_name': '\u521b\u5efa\u5bb9\u5668', 'verbose_name_plural': '\u521b\u5efa\u5bb9\u5668'},
        ),
        migrations.AddField(
            model_name='create_rongqi',
            name='iscreate',
            field=models.BooleanField(default=False, help_text='\u662f\u5426\u88ab\u521b\u5efa'),
        ),
        migrations.AlterField(
            model_name='create_rongqi',
            name='create_date',
            field=models.DateTimeField(auto_now=True, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
    ]