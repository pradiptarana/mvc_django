# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-07 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mata_pelajaran', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matapelajaran',
            name='nama_pelajaran',
            field=models.CharField(max_length=200),
        ),
    ]