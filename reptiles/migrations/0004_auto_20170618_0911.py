# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reptiles', '0003_auto_20170618_0844'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='family',
            options={'verbose_name': 'Famille', 'verbose_name_plural': 'Familles'},
        ),
        migrations.RemoveField(
            model_name='snake',
            name='venom',
        ),
        migrations.AddField(
            model_name='snake',
            name='venom',
            field=models.ManyToManyField(to='reptiles.Venom', verbose_name='Venin'),
        ),
    ]