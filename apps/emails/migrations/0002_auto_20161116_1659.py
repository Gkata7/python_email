# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 16:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='emails',
            new_name='Email',
        ),
    ]