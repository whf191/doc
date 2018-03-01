# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-29 11:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baoleiji', '0004_auto_20161228_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='mulu_sfile_dfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bieming', models.CharField(max_length=255, verbose_name='\u522b\u540d')),
                ('mulu', models.CharField(max_length=255, verbose_name='\u76ee\u5f55')),
                ('sfile', models.CharField(max_length=255, verbose_name='\u6e90\u6587\u4ef6')),
                ('dfile', models.CharField(max_length=255, verbose_name='\u76ee\u6807\u6587\u4ef6')),
                ('createdate', models.DateField(auto_now=True)),
                ('hosts_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baoleiji.hosts', verbose_name='\u7ed1\u5b9a\u4e3b\u673a')),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u76ee\u5f55\u6587\u4ef6',
                'verbose_name_plural': '\u4e3b\u673a\u76ee\u5f55\u6587\u4ef6',
            },
        ),
    ]
