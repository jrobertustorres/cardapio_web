#coding=utf8
try:
    import Image
except ImportError:
    from PIL import Image

from django.contrib.admin import site
from django.contrib.admin.options import ModelAdmin, StackedInline
from models import Album, Imagem
import base64
import MySQLdb

class ImagemInline(StackedInline):
    model                           = Imagem
    extra                           = 0
    max_num                         = 4

class AlbumAdmin(ModelAdmin):
    list_display                    = ['titulo','data_cadastro']
    inlines                         = [ImagemInline]
    search_fields                   = ['titulo',]

class ImagemAdmin(ModelAdmin):
    list_display                    = ['album', 'titulo', 'thumbnail']
    list_filter                     = ['album',]
    search_fields                   = ['titulo', 'descricao',]

    def save_model(self, request, obj, form, change):
        super(ImagemAdmin, self).save_model(request, obj, form, change)
        print obj
        if 'original' in form.changed_data:
            extensao = obj.original.name.split('.')[-1]
            obj.thumbnail = 'produto/thumbnail/%s.%s'%(obj.id, extensao)
            miniatura = Image.open(obj.original.path)
            print miniatura
            miniatura.thumbnail((100,100), Image.ANTIALIAS)
            miniatura.save(obj.thumbnail.path)

            obj.save()
            insert_imagem(obj.id,extensao)

def insert_imagem(id_imagem,extensao):
    fin = open("public/media/produto/thumbnail/"+str(id_imagem)+"."+extensao,"rb")
    print fin
    image = base64.b64encode(fin.read())
    imagem = "data:image/jpg;base64,%s" % image
    con = MySQLdb.connect("localhost","root","","cardapio_web")
    cursor = con.cursor()
    #sqlImagesb64 = "DELETE FROM empresa_empresalogob64"
    #cursor.execute(sqlImagesb64)
    sql = "INSERT INTO galeria_imagemb64(Id,imagem_b64) VALUES ('%d','%s')"%(id_imagem,imagem)

    cursor.execute(sql)
    con.commit()
    con.close()

site.register(Album, AlbumAdmin)
site.register(Imagem, ImagemAdmin)
