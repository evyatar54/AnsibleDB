# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0005_auto_20170625_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='groups',
            field=models.ManyToManyField(blank=True, to='Inventory.Group'),
        ),
    ]
