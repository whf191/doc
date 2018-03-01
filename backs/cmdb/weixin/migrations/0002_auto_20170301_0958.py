# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-01 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weixin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bind_zhuji_duankou_zhuji_ip',
            name='zhuji_duankou_id',
        ),
        migrations.RemoveField(
            model_name='bind_zhuji_duankou_zhuji_ip',
            name='zhuji_ip_id',
        ),
        migrations.RemoveField(
            model_name='zhuji_ip',
            name='zhuji_duankou_many',
        ),
        migrations.AddField(
            model_name='zhuji_duankou',
            name='zhuji_duankou_many',
            field=models.ManyToManyField(to='weixin.zhuji_ip', verbose_name='\u4e3b\u673aIP'),
        ),
        migrations.DeleteModel(
            name='bind_zhuji_duankou_zhuji_ip',
        ),
    ]
