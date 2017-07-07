# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reptiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snake',
            name='birth',
            field=models.PositiveSmallIntegerField(help_text='Année uniquement', verbose_name='Né en'),
        ),
        migrations.AlterField(
            model_name='snake',
            name='is_new_birth',
            field=models.BooleanField(default=True, verbose_name='Nouvelle naissance'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='snake',
            name='is_venomous',
            field=models.BooleanField(default=True, verbose_name='Espèce venimeuse'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='snake',
            name='no_longer_own',
            field=models.BooleanField(default=True, verbose_name='Ancienne maintenance'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='snake',
            name='reproduced',
            field=models.BooleanField(default=True, verbose_name="S'est déjà reproduit"),
            preserve_default=False,
        ),
    ]