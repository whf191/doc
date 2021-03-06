# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-10 09:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rongqi', '0007_auto_20161110_0932'),
    ]

    operations = [
        migrations.CreateModel(
            name='pipaddress_rongqi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_name', models.CharField(max_length=50, verbose_name=b'Docker\xe5\xae\xbf\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d')),
                ('ip', models.GenericIPAddressField(unique=True, verbose_name=b'Docker\xe5\xae\xbf\xe4\xb8\xbb\xe6\x9c\xbaIP')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='\u521b\u5efa\u7684\u65f6\u95f4')),
            ],
            options={
                'verbose_name': 'Docker\u5bbf\u4e3b\u673a',
                'verbose_name_plural': 'Docker\u5bbf\u4e3b\u673a',
            },
        ),
        migrations.AddField(
            model_name='ipaddress_rongqi',
            name='pipaddress_rongqi_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rongqi.pipaddress_rongqi', verbose_name=b'Docker\xe5\xae\xbf\xe4\xb8\xbb\xe6\x9c\xba'),
            preserve_default=False,
        ),
    ]
