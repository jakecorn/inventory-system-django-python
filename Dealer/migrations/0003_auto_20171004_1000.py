# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-10-04 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dealer', '0002_auto_20170929_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealer',
            name='dealer_contact_number',
            field=models.CharField(max_length=20),
        ),
    ]
