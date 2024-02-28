# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Produtorrural(models.Model):

    #__Produtorrural_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)
    cpfcnpj = models.CharField(max_length=255, null=True, blank=True)

    #__Produtorrural_FIELDS__END

    class Meta:
        verbose_name        = _("Produtorrural")
        verbose_name_plural = _("Produtorrural")


class Cultura(models.Model):

    #__Cultura_FIELDS__
    cultura = models.CharField(max_length=255, null=True, blank=True)

    #__Cultura_FIELDS__END

    class Meta:
        verbose_name        = _("Cultura")
        verbose_name_plural = _("Cultura")


class Fazenda(models.Model):

    #__Fazenda_FIELDS__
    nomefazenda = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=255, null=True, blank=True)

    #__Fazenda_FIELDS__END

    class Meta:
        verbose_name        = _("Fazenda")
        verbose_name_plural = _("Fazenda")


class Culturaplantada(models.Model):

    #__Culturaplantada_FIELDS__

    #__Culturaplantada_FIELDS__END

    class Meta:
        verbose_name        = _("Culturaplantada")
        verbose_name_plural = _("Culturaplantada")



#__MODELS__END
