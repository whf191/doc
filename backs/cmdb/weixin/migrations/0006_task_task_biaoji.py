# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-13 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weixin', '0005_zhuji_duankou_jiaoben'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_biaoji',
            field=models.CharField(blank=True, help_text='\n    \u6807\u8bc6\n      ..1 \u91cd\u542f\u5e94\u7528\u4efb\u52a1\n      ..2 \u53d1\u7248\u4efb\u52a1\n      ..3 \u56de\u6eda\u4efb\u52a1\n\n    ', max_length=10, verbose_name='\u4efb\u52a1\u6807\u8bb0'),
        ),
    ]