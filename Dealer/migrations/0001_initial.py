# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-09-29 02:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer_name', models.CharField(max_length=100)),
                ('dealer_address', models.CharField(max_length=100)),
                ('dealer_contact_number', models.IntegerField()),
                ('dealer_email', models.EmailField(max_length=254, null=True)),
            ],
            options={
                'db_table': 'dealer',
            },
        ),
    ]
