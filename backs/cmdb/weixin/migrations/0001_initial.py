# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-01 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bind_zhuji_duankou_zhuji_ip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='leixing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_created=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u4e3b\u673a\u7aef\u53e3\u7c7b\u578b')),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u7aef\u53e3\u7c7b\u578b',
                'verbose_name_plural': '\u4e3b\u673a\u7aef\u53e3\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='zhuji_duankou',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_created=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u4e3b\u673a\u7aef\u53e3')),
                ('leixing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weixin.leixing', verbose_name='\u4e3b\u673a\u7aef\u53e3\u7c7b\u578b')),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u7aef\u53e3\u7c7b\u578b',
                'verbose_name_plural': '\u4e3b\u673a\u7aef\u53e3\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='zhuji_ip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_created=True)),
                ('ip', models.GenericIPAddressField(unique=True, verbose_name='\u4e3b\u673aIP')),
                ('zhuji_duankou_many', models.ManyToManyField(through='weixin.bind_zhuji_duankou_zhuji_ip', to='weixin.zhuji_duankou')),
            ],
            options={
                'verbose_name': '\u4e3b\u673aIP',
                'verbose_name_plural': '\u4e3b\u673aIP',
            },
        ),
        migrations.AddField(
            model_name='bind_zhuji_duankou_zhuji_ip',
            name='zhuji_duankou_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weixin.zhuji_duankou'),
        ),
        migrations.AddField(
            model_name='bind_zhuji_duankou_zhuji_ip',
            name='zhuji_ip_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weixin.zhuji_ip'),
        ),
    ]
