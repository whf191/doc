# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-18 14:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gongdan', '0003_remove_shijian_create_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='shijian',
            name='create_end',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 1, 18, 14, 45, 7, 165000), help_text='\u9009\u586b', verbose_name='\u5de5\u5355\u6709\u6548\u671f'),
            preserve_default=False,
        ),
    ]
