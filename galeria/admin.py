#coding=utf8
try:
    import Image
except ImportError:
    from PIL import Image

from django.contrib.admin import site
from django.contrib.admin.options import ModelAdmin, StackedInline
from models import Album, Imagem

class ImagemInline(StackedInline):
    model                           = Imagem
    extra                           = 0
    max_num                         = 4

class AlbumAdmin(ModelAdmin):
    list_display                    = ['titulo',]
    inlines                         = [ImagemInline]
    search_fields                   = ['titulo',]

class ImagemAdmin(ModelAdmin):
    list_display                    = ['album', 'titulo', 'thumbnail']
    list_filter                     = ['album',]
    search_fields                   = ['titulo', 'descricao',]

    def save_model(self, request, obj, form, change):
        super(ImagemAdmin, self).save_model(request, obj, form, change)

        if 'original' in form.changed_data:
            extensao = obj.original.name.split('.')[-1]
            obj.thumbnail = 'original/thumbnail/%s.%s'%(obj.id, extensao)
            miniatura = Image.open(obj.foto.path)
            miniatura.thumbnail((100,100), Image.ANTIALIAS)
            miniatura.save(obj.thumbnail.path)

            obj.save()

site.register(Album, AlbumAdmin)
