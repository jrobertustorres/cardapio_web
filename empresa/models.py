#coding=utf8
from django.db.models import CharField, ImageField,TextField
import os
from util.models import Padrao

class Empresa(Padrao):
    class Meta:
        verbose_name                = u'Empresa'
        verbose_name_plural         = u'Empresas'
    razao_social                    = CharField(verbose_name=u'Razão Social',max_length=100,blank=True,null=True)
    nome_fantasia                   = CharField(verbose_name=u'Nome Fantasia',max_length=100,blank=True,null=True)
    foto                            = ImageField(verbose_name=u'Foto Original',upload_to='logo/original',max_length=255,blank=True,null=True)
    thumbnail                       = ImageField(verbose_name=u'Foto Thumbnail',upload_to='logo/thumbnail',max_length=255,blank=True,null=True,editable=False)
    imagem_b64                      = TextField(verbose_name=u'Foto B64',blank=True,null=True)

    def __unicode__(self):
        return u'%s'%self.nome_fantasia

    def logo(self):
        return '<img src="%s" width="100" height="100">' % self.thumbnail.url
    logo.short_description = 'Logo'
    logo.allow_tags = True
