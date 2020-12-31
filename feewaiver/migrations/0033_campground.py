# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-29 03:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feewaiver', '0032_auto_20201224_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampGround',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=256)),
                ('park', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feewaiver.Park')),
            ],
        ),
    ]