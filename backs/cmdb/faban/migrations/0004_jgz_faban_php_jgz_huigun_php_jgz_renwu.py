# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-02 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faban', '0003_auto_20170317_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='jgz_faban_php',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faban_leixing', models.CharField(max_length=255, verbose_name='\u67b6\u6784\u7ec4\u4f20\u8fc7\u6765\u7684\u53d1\u7248\u7c7b\u578b')),
                ('url_zip', models.URLField(verbose_name='url\u4e0b\u8f7d\u8def\u5f84')),
                ('url_zip_md5', models.CharField(max_length=255, verbose_name='url_zip\u7684md5')),
                ('faban_id', models.CharField(max_length=255, verbose_name='\u4f20\u8fc7\u6765\u7684ID')),
                ('state', models.CharField(max_length=1, verbose_name='\u53d1\u7248\u72b6\u6001\uff0c1\u662f\u6b63\u5e38 3\u662f\u6b63\u5e38\u5df2\u53d1')),
                ('create_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u67b6\u6784\u7ec4\u65b0\u53d1\u7248',
                'verbose_name_plural': '\u67b6\u6784\u7ec4\u65b0\u53d1\u7248',
            },
        ),
        migrations.CreateModel(
            name='jgz_huigun_php',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faban_id', models.CharField(max_length=255, verbose_name='\u56de\u6eda\u4f20\u8fc7\u6765\u7684ID')),
                ('state', models.CharField(max_length=1, verbose_name='\u56de\u6eda\u72b6\u6001,2\u662f\u56de\u6eda\uff0c4\u662f\u56de\u6eda\u5df2\u53d1')),
                ('create_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u67b6\u6784\u7ec4\u56de\u6eda\u53d1\u7248',
                'verbose_name_plural': '\u67b6\u6784\u7ec4\u56de\u6eda\u53d1\u7248',
            },
        ),
        migrations.CreateModel(
            name='jgz_renwu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faban_id', models.CharField(max_length=255, verbose_name='\u4f20\u8fc7\u6765\u7684ID')),
                ('state', models.CharField(max_length=1, verbose_name='\u72b6\u6001,1\u662f\u6b63\u5e38\u53d1\u7248\uff0c2\u662f\u56de\u6eda')),
                ('jilu_log', models.CharField(max_length=255, verbose_name='\u65e5\u5fd7\u8bb0\u5f55\u6587\u4ef6')),
                ('create_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u67b6\u6784\u7ec4\u4efb\u52a1\u8bb0\u5f55',
                'verbose_name_plural': '\u67b6\u6784\u7ec4\u4efb\u52a1\u8bb0\u5f55',
            },
        ),
    ]