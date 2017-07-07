#-*- coding: utf-8 -*-
from django.db import models
from .utils import Distribution, Biotop
from django.template.defaultfilters import slugify

class Reptile(models.Model):
    """ Similar for all reptiles """
    LIFE_STYLES = (
        ('A', 'Aube'),
        ('D', 'Diurne'),
        ('C', 'Crépusculaire'),
        ('N', 'Nocturne')
    )
    BUSINESS_T = (
        ('A', 'Achat'),
        ('V', 'Vente'),
        ('E', 'Echange')
    )
    scientific_name = models.CharField(max_length=128, verbose_name='Nom scientifique', unique=True)
    slug = models.SlugField(unique=True)
    sex = models.CharField(max_length=33, verbose_name='Sexe', help_text='format: n.n')
    birth = models.PositiveSmallIntegerField(verbose_name='Né en', help_text='Année uniquement')
    reproduced = models.BooleanField(verbose_name='S\'est déjà reproduit')
    qt_born = models.PositiveSmallIntegerField(verbose_name='Nombre de naissance')
    is_new_birth = models.BooleanField(verbose_name='Nouvelle naissance')
    no_longer_own = models.BooleanField(verbose_name='Ancienne maintenance')
    distribution = models.ManyToManyField(Distribution, verbose_name='Air de répartition')
    biotop = models.ManyToManyField(Biotop, verbose_name='Environnement')
    life_style = models.CharField(max_length=1, verbose_name='mode de vie', choices=LIFE_STYLES)
    description = models.TextField(blank=True)
    business = models.CharField(max_length=1, blank=True, verbose_name='Ventes et achats', choices=BUSINESS_T)
    price = models.FloatField(blank=True)

    class Meta:
        abstract = True
        verbose_name = "Reptile"
        verbose_name_plural = "Reptiles"

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.reproduced is not None and self.qt_born is None:
            raise ValidationError('Le nombre de naissance est obligatoire si des reproductions ont été définies')
        if self.business is not None and self.price is None:
            raise ValidationError('La valeure marchande doit être définie si \'ventes et achats\' a été définit')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.scientific_name)
        super(Reptile, self).save(*args, **kwargs)