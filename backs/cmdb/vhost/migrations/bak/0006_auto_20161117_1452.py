# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-17 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vhost', '0005_auto_20161117_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guanli_vhost',
            name='login_pass',
        ),
        migrations.RemoveField(
            model_name='guanli_vhost',
            name='login_user',
        ),
    ]