# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-25 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baishi', '0003_auto_20170325_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piliang_xuesheng_jiazhang_daoru',
            name='banji_leixing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baishi.banji', verbose_name='\u73ed\u7ea7\u7c7b\u578b'),
        ),
    ]