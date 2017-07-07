# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reptiles', '0002_auto_20170618_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snake',
            name='biotop',
        ),
        migrations.AddField(
            model_name='snake',
            name='biotop',
            field=models.ManyToManyField(to='reptiles.Biotop', verbose_name='Environnement'),
        ),
        migrations.RemoveField(
            model_name='snake',
            name='distribution',
        ),
        migrations.AddField(
            model_name='snake',
            name='distribution',
            field=models.ManyToManyField(to='reptiles.Distribution', verbose_name='Air de répartition'),
        ),
    ]