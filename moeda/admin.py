#coding=utf8

from django.contrib.admin import ModelAdmin, site
from models import Moeda

class MoedaAdmin(ModelAdmin):
    list_display = ['nome_moeda','sigla_moeda','data_cadastro']

site.register(Moeda,MoedaAdmin)