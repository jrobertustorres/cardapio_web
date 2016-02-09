#coding=utf8

from django.contrib.admin import ModelAdmin, site, TabularInline
from models import Produto, Categoria

#import base64
#import MySQLdb

"""class ImagemInline(admin.TabularInline):
    model = Produto"""

class ProdutoAdmin(ModelAdmin):
    list_display = ['nome','descricao','preco','categoria','ativo']
    #inlines = [ImagemInline]
    #form = FormImagem

class CategoriaAdmin(ModelAdmin):
    list_display                    = ['nome','ativo']

"""class ImagemInline(admin.TabularInline):
    model = Imagem
    extra = 1"""

site.register(Produto,ProdutoAdmin)
site.register(Categoria,CategoriaAdmin)