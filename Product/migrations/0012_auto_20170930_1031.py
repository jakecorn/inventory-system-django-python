# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-09-30 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0011_auto_20170930_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_quantity',
            field=models.FloatField(),
        ),
    ]
