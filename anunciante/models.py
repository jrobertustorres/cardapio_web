#coding=utf8

from django.db.models import CharField, ImageField,BinaryField,ForeignKey,BooleanField,DateTimeField,IntegerField
from util.models import Padrao
from geo.models import Cidade,Estado

class Anunciante(Padrao):
    class Meta:
        verbose_name                = u'Anunciante'
        verbose_name_plural         = u'Anunciantes'
    razao_social                    = CharField(verbose_name=u'Razão Social',max_length=100,blank=True,null=True)
    nome_fantasia                   = CharField(verbose_name=u'Nome Fantasia',max_length=100,blank=False,null=False)
    cnpj                            = CharField(verbose_name=u'CNPJ',max_length=20,)
    telefone                        = CharField(verbose_name=u'Telefone',max_length=20,blank=True,null=True)
    email                           = CharField(verbose_name=u'E-mail',max_length=40,blank=True,null=True)
    endereco                        = CharField(verbose_name=u'Logradouro',max_length=100,blank=True,null=True)
    numero                          = CharField(verbose_name=u'Número',max_length=100,blank=True,null=True)
    complemento                     = CharField(verbose_name=u'Complemento',max_length=100,blank=True,null=True)
    cidade                          = ForeignKey(Cidade,verbose_name=u'Cidade')
    estado                          = ForeignKey(Estado,verbose_name=u'Estado')
    ativo                           = BooleanField(verbose_name=u'Ativo')
    data_ativacao                   = DateTimeField(verbose_name=u'Data para ativação do anúncio',help_text=u'Data inicial para execução do anúncio.')
    data_desativacao                = DateTimeField(verbose_name=u'Data para desativar anúncio',help_text=u'Data final para execução do anúncio.')
    banner                          = ImageField(verbose_name=u'Banner',upload_to='anunciante/original',max_length=255,blank=True,null=True)
    thumbnail                       = ImageField(verbose_name=u'Banner Miniatura',upload_to='anunciante/thumbnail',max_length=255,blank=True,null=True,editable=True)
    tempo_visivel                   = IntegerField(verbose_name=u'Tempo do banner.',help_text=u'Tempo em segundos que o banner ficará visível.')

    def __unicode__(self):
        return u'%s'%self.nome_fantasia

    def logo(self):
        return '<img src="%s" width="100" height="100">' % self.thumbnail.url
    logo.short_description = 'Logo'
    logo.allow_tags = True

class AnuncianteBannerB64(Padrao):
    imagem_b64                      = BinaryField(blank=True,null=True,editable=False)
