# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-15 09:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rongqi', '0011_auto_20161111_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='shenqing_rongqi',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2016, 11, 15, 9, 6, 53, 141000)),
            preserve_default=False,
        ),
    ]
