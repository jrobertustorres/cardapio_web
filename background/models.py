#coding=utf8

from django.db.models import ImageField,TextField
from util.models import Padrao

class PlanoDeFundo(Padrao):
    class Meta:
        verbose_name                = u'Plano de Fundo'
        verbose_name_plural         = u'Planos de Fundo'
    foto                            = ImageField(verbose_name=u'Plano de Fundo',upload_to='background/original',max_length=255,blank=True,null=True)
    thumbnail                       = ImageField(upload_to='background/thumbnail',blank=True,null=True,editable=False)
    imagem_b64                      = TextField(blank=True,null=True,editable=False)

    def __unicode__(self):
        return u'%s'%self.verbose_name

    def plano_de_fundo(self):
        return '<img src="%s" width="100" height="100">' % self.thumbnail.url
    plano_de_fundo.short_description = 'Logo'
    plano_de_fundo.allow_tags = True
