# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-04 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leixing', models.CharField(max_length=30)),
                ('neirong', models.TextField()),
            ],
            options={
                'verbose_name': '\u65e5\u5fd7\u91c7\u96c6',
                'verbose_name_plural': '\u65e5\u5fd7\u91c7\u96c6',
            },
        ),
    ]
