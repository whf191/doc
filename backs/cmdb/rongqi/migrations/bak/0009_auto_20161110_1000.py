# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-10 10:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rongqi', '0008_auto_20161110_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guanli_rongqi',
            name='rongqi_ip',
            field=models.OneToOneField(help_text='\u586b\u5199\u5bb9\u5668\u7684\u5916\u90e8ip\u5730\u5740', on_delete=django.db.models.deletion.CASCADE, to='rongqi.ipaddress_rongqi', verbose_name='\u5bb9\u5668\u7ed1\u5b9a\u7684IP'),
        ),
    ]
