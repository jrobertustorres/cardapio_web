#coding=utf8
from django.db.models import CharField
from util.models import Padrao

class Moeda(Padrao):
    class Meta:
        verbose_name                = u'Moeda'
        verbose_name_plural         = u'Moedas'
    nome_moeda                      = CharField(verbose_name=u'Moeda',max_length=20)
    sigla_moeda                     = CharField(verbose_name=u'Sigla',max_length=2)

    def __unicode__(self):
        return u'%s'%self.nome_moeda