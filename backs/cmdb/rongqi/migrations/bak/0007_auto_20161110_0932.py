# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-10 09:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rongqi', '0006_auto_20161109_1004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duankou_rongqi',
            name='shenqing_rongqi_id',
        ),
        migrations.DeleteModel(
            name='duankou_rongqi',
        ),
    ]