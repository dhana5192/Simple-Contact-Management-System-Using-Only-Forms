# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-08 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='alt_mobile_no',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobile_no',
            field=models.CharField(max_length=12),
        ),
    ]
