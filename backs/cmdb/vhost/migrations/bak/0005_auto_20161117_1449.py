# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-17 14:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vhost', '0004_auto_20161117_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guanli_vhost',
            old_name='shenqing_rongqi_id',
            new_name='shenqing_vhost_id',
        ),
    ]
