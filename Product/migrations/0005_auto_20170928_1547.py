# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-09-28 07:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_auto_20170927_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.CharField(max_length=100, validators=[django.core.validators.EmailValidator('errorrrorror')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_quantity',
            field=models.IntegerField(max_length=100),
        ),
    ]
