# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-03 10:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feewaiver', '0011_feewaiver_parks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feewaiverlogentry',
            old_name='approval',
            new_name='fee_waiver',
        ),
    ]