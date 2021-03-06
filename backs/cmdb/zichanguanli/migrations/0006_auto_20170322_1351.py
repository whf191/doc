# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-22 13:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zichanguanli', '0005_feiyong_leixing_fufei_fangshi_qingkuan_mingxi'),
    ]

    operations = [
        migrations.AddField(
            model_name='qingkuan_mingxi',
            name='fapiao_leixing',
            field=models.CharField(blank=True, max_length=255, verbose_name='\u53d1\u7968\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='qingkuan_mingxi',
            name='guishu_bumen',
            field=models.CharField(blank=True, max_length=255, verbose_name='\u5f52\u5c5e\u90e8\u95e8'),
        ),
        migrations.AddField(
            model_name='qingkuan_mingxi',
            name='hanshui_danjia',
            field=models.CharField(blank=True, max_length=255, verbose_name='\u542b\u7a0e\u5355\u4ef7'),
        ),
        migrations.AddField(
            model_name='qingkuan_mingxi',
            name='hanshui_heji',
            field=models.CharField(blank=True, max_length=255, verbose_name='\u542b\u7a0e\u5408\u8ba1'),
        ),
        migrations.AddField(
            model_name='qingkuan_mingxi',
            name='jiage_danwei',
            field=models.CharField(blank=True, max_length=255, verbose_name='\u52a0\u4e2a\u5355\u4f4d'),
        ),
        migrations.AddField(
            model_name='qingkuan_mingxi',
            name='jiliang_danwei',
            field=models.CharField(blank=True, max_length=255, verbose_name='\u8ba1\u91cf\u5355\u4f4d'),
        ),
        migrations.AddField(
            model_name='qingkuan_mingxi',
            name='shuilv',
            field=models.CharField(blank=True, max_length=255, verbose_name='\u7a0e\u7387'),
        ),
        migrations.AddField(
            model_name='qingkuan_mingxi',
            name='shuliang',
            field=models.CharField(blank=True, max_length=255, verbose_name='\u6570\u91cf'),
        ),
        migrations.AlterField(
            model_name='qingkuan_mingxi',
            name='fufei_fangshi_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='zichanguanli.fufei_fangshi', verbose_name='\u4ed8\u8d39\u65b9\u5f0f'),
        ),
        migrations.AlterField(
            model_name='qingkuan_mingxi',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='\u8bf7\u6b3e\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='qingkuan_mingxi',
            name='note',
            field=models.TextField(blank=True, verbose_name='\u5907\u6ce8'),
        ),
        migrations.AlterField(
            model_name='qingkuan_mingxi',
            name='shifou_qianding_hetong',
            field=models.CharField(blank=True, max_length=255, verbose_name='\u5408\u540c\u5230\u671f\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='qingkuan_mingxi',
            name='yongtu',
            field=models.CharField(blank=True, max_length=255, verbose_name='\u7528\u9014'),
        ),
        migrations.AlterField(
            model_name='qingkuan_mingxi',
            name='zhifu_jine_fanwei',
            field=models.CharField(blank=True, max_length=255, verbose_name='\u652f\u4ed8\u91d1\u989d\u8303\u56f4'),
        ),
    ]
