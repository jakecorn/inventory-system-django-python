# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-09-30 02:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0010_auto_20170930_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100),
        ),
    ]