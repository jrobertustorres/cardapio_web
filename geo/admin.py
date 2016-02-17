#-*- coding:utf-8 -*-
from models import *
from django.contrib import admin
from settings import STATIC_URL

class PaisAdmin(admin.ModelAdmin):
    list_display        = ['nome']
    search_fields       = ['nome']
    list_per_page       = 10

class EstadoAdmin(admin.ModelAdmin):
    list_display        = ['nome','uf']
    search_fields       = ['nome','pais__nome']
    list_per_page       = 10

class CidadeAdmin(admin.ModelAdmin):
    class Media: js     = (STATIC_URL+'js/list_sortable_admin.js',)
    prepopulated_fields = {'slug':('nome',)}
    list_display        = ['nome','estado','slug','cod_ibge','dat_ativacao','ativo','ordem']
    search_fields       = ['nome','estado__nome','pais__nome','cod_ibge','slug']
    list_editable       = ['ordem']
    list_per_page       = 10

admin.site.register(Pais,PaisAdmin)
admin.site.register(Estado,EstadoAdmin)
admin.site.register(Cidade,CidadeAdmin)