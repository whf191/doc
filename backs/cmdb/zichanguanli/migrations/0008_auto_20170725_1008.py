# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-25 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zichanguanli', '0007_auto_20170329_1621'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guishu_bumen',
            options={'verbose_name': '\u6700\u7ec8\u5f52\u5c5e\u90e8\u95e8', 'verbose_name_plural': '\u6700\u7ec8\u5f52\u5c5e\u90e8\u95e8'},
        ),
        migrations.AlterField(
            model_name='zuzhuang_taishi_diannao',
            name='create_date',
            field=models.DateTimeField(auto_now=True, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
    ]
