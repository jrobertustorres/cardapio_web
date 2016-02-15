#coding=utf8

from django.db.models import CharField, ImageField,BinaryField,ForeignKey
from util.models import Padrao
from geo.models import Cidade,Estado

class Empresa(Padrao):
    class Meta:
        verbose_name                = u'Empresa'
        verbose_name_plural         = u'Empresas'
    razao_social                    = CharField(verbose_name=u'Razão Social',max_length=100,blank=True,null=True)
    nome_fantasia                   = CharField(verbose_name=u'Nome Fantasia',max_length=100,blank=True,null=True)
    cnpj                            = CharField(verbose_name=u'CNPJ',max_length=20,)
    endereco                        = CharField(verbose_name=u'Logradouro',max_length=100,blank=True,null=True)
    numero                          = CharField(verbose_name=u'Número',max_length=100,blank=True,null=True)
    complemento                     = CharField(verbose_name=u'Complemento',max_length=100,blank=True,null=True)
    cidade                          = ForeignKey(Cidade,verbose_name=u'Cidade')
    estado                          = ForeignKey(Estado,verbose_name=u'Estado')
    foto                            = ImageField(verbose_name=u'Logo do Estabelecimento',upload_to='logo_empresa/original',max_length=255,blank=True,null=True)
    thumbnail                       = ImageField(verbose_name=u'Logo Miniatura',upload_to='logo_empresa/thumbnail',max_length=255,blank=True,null=True,editable=True)

    def __unicode__(self):
        return u'%s'%self.nome_fantasia

    def logo(self):
        return '<img src="%s" width="100" height="100">' % self.thumbnail.url
    logo.short_description = 'Logo'
    logo.allow_tags = True

class EmpresaLogoB64(Padrao):
    imagem_b64                      = BinaryField(blank=True,null=True,editable=False)
