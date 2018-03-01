# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-16 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rongqi', '0014_auto_20161115_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='pipaddress_rongqi',
            name='password',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u5bbf\u4e3b\u673a\u5bc6\u7801'),
        ),
        migrations.AlterField(
            model_name='pipaddress_rongqi',
            name='ip',
            field=models.GenericIPAddressField(unique=True, verbose_name='Docker\u5bbf\u4e3b\u673aIP'),
        ),
        migrations.AlterField(
            model_name='pipaddress_rongqi',
            name='ip_name',
            field=models.CharField(max_length=50, verbose_name='Docker\u5bbf\u4e3b\u673a\u540d'),
        ),
    ]