# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-30 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporters',
            name='mobile',
            field=models.IntegerField(verbose_name='手机号'),
        ),
    ]
