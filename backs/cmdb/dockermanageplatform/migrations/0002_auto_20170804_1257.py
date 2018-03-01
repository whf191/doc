# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-04 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dockermanageplatform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='managecontainer',
            name='container_password',
            field=models.CharField(blank=True, default='123456', max_length=255, null=True, verbose_name='\u5bb9\u5668\u5bc6\u7801'),
        ),
        migrations.AddField(
            model_name='managecontainer',
            name='container_username',
            field=models.CharField(blank=True, default='root', max_length=255, null=True, verbose_name='\u5bb9\u5668\u7528\u6237\u540d'),
        ),
    ]
