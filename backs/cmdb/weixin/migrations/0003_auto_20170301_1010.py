# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-01 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weixin', '0002_auto_20170301_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('task_id', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='\u4efb\u52a1ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='\u4efb\u52a1\u6807\u9898')),
                ('context', models.TextField(blank=True, verbose_name='\u4efb\u52a1\u4e0a\u4e0b\u6587')),
                ('username', models.CharField(max_length=20, verbose_name='\u4efb\u52a1\u7528\u6237')),
                ('task_zhuangtai', models.CharField(blank=True, max_length=10, null=True, verbose_name='\u4efb\u52a1\u72b6\u6001')),
                ('task_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='zhuji_duankou',
            options={'verbose_name': '\u4e3b\u673a\u7aef\u53e3', 'verbose_name_plural': '\u4e3b\u673a\u7aef\u53e3'},
        ),
        migrations.AlterField(
            model_name='leixing',
            name='create_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='zhuji_duankou',
            name='create_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='zhuji_ip',
            name='create_date',
            field=models.DateField(auto_now=True),
        ),
    ]
