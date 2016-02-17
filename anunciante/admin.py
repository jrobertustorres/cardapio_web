#coding=utf8
try:
    import Image
except ImportError:
    from PIL import Image

from django.contrib.admin import ModelAdmin,site
from anunciante.models import Anunciante

import base64
import MySQLdb

class AnuncianteAdmin(ModelAdmin):
    list_display                    = ['nome_fantasia','data_cadastro']
    list_filter                     = ['nome_fantasia']

    """Metodo declarado para criar miniatura da imagem depois de salvar"""
    def save_model(self, request, obj, form, change):
        super(AnuncianteAdmin, self).save_model(request, obj, form, change)

        if 'banner' in form.changed_data:
            extensao = obj.banner.name.split('.')[-1]
            obj.thumbnail = 'anunciante/thumbnail/%s.%s'%(obj.id, extensao)
            miniatura = Image.open(obj.banner.path)
            miniatura.thumbnail((100,100), Image.ANTIALIAS)
            miniatura.save(obj.thumbnail.path)

            obj.save()
            insert_banner(obj.id,extensao)
        return obj

def insert_banner(id_imagem,extensao):
    fin = open("public/media/anunciante/thumbnail/"+str(id_imagem)+"."+extensao,"rb")
    print fin
    image = base64.b64encode(fin.read())
    imagem = "data:image/jpg;base64,%s" % image
    con = MySQLdb.connect("localhost","root","","cardapio_web")
    cursor = con.cursor()
    sqlImagesb64 = "DELETE FROM anunciante_anunciantebannerb64"
    cursor.execute(sqlImagesb64)
    sql = "INSERT INTO anunciante_anunciantebannerb64(Id,imagem_b64) VALUES ('%d','%s')"%(id_imagem,imagem)

    cursor.execute(sql)
    con.commit()
    con.close()

site.register(Anunciante,AnuncianteAdmin)

