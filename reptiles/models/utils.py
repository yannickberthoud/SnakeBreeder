#-*- coding: utf-8 -*-
from django.db import models

class Distribution(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='nom')

    class Meta:
        verbose_name = "Distribution"
        verbose_name_plural = "Distributions"

    def __str__(self):
        return self.name

class Biotop(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='nom')

    class Meta:
        verbose_name = "Biotope"
        verbose_name_plural = "Biotopes"

    def __str__(self):
        return self.name