# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 01:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0012_auto_20170626_0130'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='role',
            name='id',
        ),
        migrations.AlterField(
            model_name='group',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='roles',
            field=models.ManyToManyField(blank=True, through='Inventory.GroupRoles', to='Inventory.Role'),
        ),
        migrations.AlterField(
            model_name='role',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='grouproles',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.Group'),
        ),
        migrations.AddField(
            model_name='grouproles',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.Role'),
        ),
    ]
