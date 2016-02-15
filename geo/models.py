#-*- coding:utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Pais(models.Model):
    class Meta:
        verbose_name        = _(u'País')
        verbose_name_plural = _(u'Países')
    nome                    = models.CharField(_(u'Nome'), max_length=128)
    def __unicode__(self):  return u'%s'%self.nome

class Estado(models.Model):
    class Meta:
        verbose_name        = _(u'Estado')
        verbose_name_plural = _(u'Estados')
    pais                    = models.ForeignKey(Pais,verbose_name=_(u'País'),related_name='estado')
    nome                    = models.CharField(verbose_name=_(u'Nome'),max_length=80)
    def __unicode__(self):  return u'%s'%self.nome

class Cidade(models.Model):
    class Meta:
        verbose_name        = _(u'Cidade')
        verbose_name_plural = _(u'Cidades')
        ordering            = ('ordem',)
    estado                  = models.ForeignKey(Estado,verbose_name=_(u'Estado'),related_name='cidade')
    nome                    = models.CharField(_(u'Nome'), max_length=60)
    slug                    = models.SlugField(max_length=100,db_index=True,unique=True)
    dat_ativacao            = models.DateTimeField(verbose_name=_(u'Data de Ativação'),blank=True,null=True,help_text=_(u'Coloque uma data para ativar a cidade'))
    ordem                   = models.PositiveIntegerField(blank=True,null=True)
    cod_ibge                = models.IntegerField(verbose_name=_(u'Código IBGE'),blank=True,null=True,db_index=True)
    def __unicode__(self): return u'%s'%self.nome
    def ativo(self): return bool(self.dat_ativacao)
    ativo.boolean = True