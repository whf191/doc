# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-28 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baoleiji', '0003_auto_20161212_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hosts',
            name='hostport',
            field=models.IntegerField(default=22, verbose_name='SSH\u7aef\u53e3'),
        ),
        migrations.AlterField(
            model_name='shenji',
            name='createdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
