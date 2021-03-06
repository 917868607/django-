# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-26 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailmodels',
            options={'verbose_name': '邮箱验证', 'verbose_name_plural': '邮箱验证'},
        ),
        migrations.AddField(
            model_name='emailmodels',
            name='send_type',
            field=models.CharField(choices=[('register', '注册邮件'), ('forget', '找回密码')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
