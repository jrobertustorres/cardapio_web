#coding=utf8

from django.db.models import ImageField,BinaryField,CharField
from util.models import Padrao

class PlanoDeFundo(Padrao):
    class Meta:
        verbose_name                = u'Plano de Fundo'
        verbose_name_plural         = u'Plano de Fundo'
    descricao                       = CharField(verbose_name=u'Descrição',max_length=100,blank=False,null=False)
    foto                            = ImageField(verbose_name=u'Plano de Fundo',upload_to='background/original',max_length=255,blank=False,null=False)
    thumbnail                       = ImageField(verbose_name=u'Planos de Fundo Miniatura',upload_to='background/thumbnail',blank=False,null=False)

    def __unicode__(self):
        return u'%s'%self.descricao

    def plano_de_fundo(self):
        return '<img src="%s" width="100" height="100">' % self.thumbnail.url
    plano_de_fundo.short_description = 'Logo'
    plano_de_fundo.allow_tags = True

class PlanoDeFundoB64(Padrao):
    imagem_b64                      = BinaryField(blank=True,null=True,editable=False)