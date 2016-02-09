#coding=utf8
from datetime import datetime
from django.db import models
from django.db.models import ForeignKey, DateTimeField, TextField, CharField, SlugField
from sorl.thumbnail import ImageField
from produto.models import Produto
from util.models import Padrao

class Album(Padrao):
    """Um album eh um pacote de imagens, ele tem um titulo e um
   slug para sua identificacao."""

    class Meta:
        verbose_name                = u'Album'
        verbose_name_plural         = u'Albuns'
        ordering = ('titulo',)
    titulo = CharField(max_length=100)
    produto                         = ForeignKey(Produto,verbose_name=u'Produto')
    slug = SlugField(
        max_length=100,
        blank=True,
        unique=True
    )

    def __unicode__(self):
        return self.titulo


class Imagem(models.Model):
    """Cada instancia desta classe contem uma imagem da galeria,
   com seu respectivo thumbnail (miniatura) e imagem em tamanho
   natural. Varias imagens podem conter dentro de um Album"""

    class Meta:
        verbose_name                = u'Imagem'
        verbose_name_plural         = u'Imagens'
        ordering = ('album', 'titulo',)
    album = ForeignKey('Album')
    titulo = CharField(max_length=100)
    slug = SlugField(
        max_length=100,
        blank=True,
        unique=True
    )
    descricao = TextField(blank=True)
    original = ImageField(
        verbose_name=u'Foto Original',
        max_length=255,
        null=True,
        blank=True,
        upload_to='produto/original',
    )

    thumbnail = ImageField(
        verbose_name=u'Foto Miniatura',
        max_length=255,
        null=True,
        blank=True,
        upload_to='produto/thumbnail',
        editable=False
    )
    publicacao = DateTimeField(
        default=datetime.now,
        blank=True
    )

    def __unicode__(self):
        return self.titulo