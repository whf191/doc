# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-02 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_webshell', '0004_auto_20170702_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host_type',
            name='url',
            field=models.CharField(max_length=255, verbose_name='\u5bfc\u822aurl'),
        ),
    ]
