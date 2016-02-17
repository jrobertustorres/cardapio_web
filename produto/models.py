#coding=utf8
from util.models import Padrao
from django.db.models import CharField, FloatField, BooleanField, ForeignKey

class Categoria(Padrao):
    class Meta:
        verbose_name                = u'Categoria'
        verbose_name_plural         = u'Categorias'
    nome                            = CharField(verbose_name=u'Nome',max_length=100)
    ativo                           = BooleanField(verbose_name=u'Ativo',default=1)

    def __unicode__(self):
        return u'%s'%self.nome

class Produto(Padrao):
    class Meta:
        verbose_name                = u'Produto'
        verbose_name_plural         = u'Produtos'
    nome                            = CharField(verbose_name=u'Nome',max_length=100)
#    slug                            = SlugField(max_length=100, blank=True, unique=True)
    descricao                       = CharField(verbose_name=u'Descrição',max_length=100,blank=True,null=True)
    preco                           = FloatField(verbose_name=u'Preço',blank=True,null=True)
    ativo                           = BooleanField(verbose_name=u'Ativo')
    categoria                       = ForeignKey(Categoria,verbose_name=u'Categoria')

    def __unicode__(self):
        return u'%s'%self.nome


