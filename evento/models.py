#coding=utf8

from django.db.models import CharField, ImageField,BinaryField,ForeignKey,BooleanField,DateTimeField,IntegerField
from util.models import Padrao
from geo.models import Cidade,Estado

class Evento(Padrao):
    class Meta:
        verbose_name                = u'Evento'
        verbose_name_plural         = u'Eventos'
    nome                            = CharField(verbose_name=u'Nome do Evento',max_length=100)
    data_evento                     = DateTimeField(verbose_name=u'Data do Evento')
    banner                          = ImageField(verbose_name=u'Banner',upload_to='evento/original',max_length=255,blank=True,null=True)
    thumbnail                       = ImageField(verbose_name=u'Banner Miniatura',upload_to='evento/thumbnail',max_length=255,blank=True,null=True,editable=True)

    def __unicode__(self):
        return u'%s'%self.nome

class EventoBannerB64(Padrao):
    imagem_b64                      = BinaryField(blank=True,null=True,editable=False)
