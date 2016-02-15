#coding=utf8

from django.contrib.admin import ModelAdmin, site
from models import Produto, Categoria

class ProdutoAdmin(ModelAdmin):
    list_display                    = ['nome','descricao','preco','categoria','ativo']
    list_filter                     = ['nome','categoria']
    #inlines = [ImagemInline]
    #form = FormImagem

class CategoriaAdmin(ModelAdmin):
    list_display                    = ['nome','ativo']
    list_filter                     = ['nome']

"""class ImagemInline(admin.TabularInline):
    model = Imagem
    extra = 1"""

site.register(Produto,ProdutoAdmin)
site.register(Categoria,CategoriaAdmin)