# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-21 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyinotifys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zi_lujing',
            name='fu_lujing_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pyinotifys.fu_lujing', verbose_name='\u7236\u8def\u5f84'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='zi_lujing',
            name='name',
            field=models.CharField(help_text='\u5b50\u8def\u5f84\u7684\u76ee\u7684\u5bf9\u5e94\u6392\u9664', max_length=255, verbose_name='\u5b50\u8def\u5f84'),
        ),
    ]
