# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-31 02:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20180831_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporters',
            name='Company_Id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Company', verbose_name='公司'),
        ),
        migrations.AlterField(
            model_name='reporters',
            name='Industry_Id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Industry', verbose_name='行业'),
        ),
        migrations.AlterField(
            model_name='reporters',
            name='Manuscript_Id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Manuscript', verbose_name='历史稿件'),
        ),
    ]