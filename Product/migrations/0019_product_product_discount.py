# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-10-03 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0018_auto_20171002_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_discount',
            field=models.FloatField(default=0),
        ),
    ]