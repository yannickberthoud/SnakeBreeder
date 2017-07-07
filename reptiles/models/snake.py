#-*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify

from .base import Reptile


class Family(models.Model):
    name = models.CharField(max_length=24, verbose_name='Nom', unique=True,)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Famille"
        verbose_name_plural = "Familles"

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super(Family, self).save(*args, **kwargs)

class Dentition(models.Model):
    name = models.CharField(max_length=24, unique=True, verbose_name='nom')
    description = models.TextField()

    class Meta:
        verbose_name = "Dentition"
        verbose_name_plural = "Dentitions"

    def __str__(self):
        return self.name

class Venom(models.Model):
    name = models.CharField(max_length=12, unique=True, verbose_name='nom')
    description = models.TextField()

    class Meta:
        verbose_name = "Venin"
        verbose_name_plural = "Venins"

    def __str__(self):
        return self.name

class Snake(Reptile):
    """ Schemas for Snake """
    REPRODUCTIONS = (
        ('O', 'Ovipare'),
        ('V', 'Vivipare'),
    )
    family = models.ForeignKey(Family, on_delete=models.CASCADE, verbose_name='Famille')
    dentition = models.ForeignKey(Dentition)
    reproduction = models.CharField(max_length=1, choices=REPRODUCTIONS)
    is_venomous = models.BooleanField(verbose_name='Espèce venimeuse')
    venom = models.ManyToManyField(Venom, verbose_name='Venin')

    class Meta:
        verbose_name = "Serpent"
        verbose_name_plural = "Serpents"

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.is_venomous is not None and self.venom is None:
            raise ValidationError("Le type de venin doit être définit si l'espèce est marquée comme étant venimeuse")

    def __str__(self):
        return self.scientific_name

    def get_absolute_url(self):
        from django.urls import reverse
        pass