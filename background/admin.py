#coding=utf8
try:
    import Image
except ImportError:
    from PIL import Image

from django.contrib.admin import ModelAdmin,site
from background.models import PlanoDeFundo

import base64
import MySQLdb

class PlanoDeFundoAdmin(ModelAdmin):
    list_display = ['descricao','data_cadastro']

    """Metodo declarado para criar miniatura da imagem depois de salvar"""
    def save_model(self, request, obj, form, change):
        super(PlanoDeFundoAdmin, self).save_model(request, obj, form, change)

        if 'foto' in form.changed_data:
            extensao = obj.foto.name.split('.')[-1]
            obj.thumbnail = 'background/thumbnail/%s.%s'%(obj.id, extensao)
            miniatura = Image.open(obj.foto.path)
            miniatura.thumbnail((800,600), Image.ANTIALIAS)
            miniatura.save(obj.thumbnail.path)

            obj.save()
            insert_background(obj.id,extensao)

def insert_background(id_imagem,extensao):
    fin = open("public/media/background/thumbnail/"+str(id_imagem)+"."+extensao,"rb")
    image = base64.b64encode(fin.read())
    imagem = "data:image/jpg;base64,%s" % image
    con = MySQLdb.connect("localhost","root","","cardapio_web")
    cursor = con.cursor()
    sqlImagesb64 = "DELETE FROM background_planodefundob64"
    cursor.execute(sqlImagesb64)
    sql = "INSERT INTO background_planodefundob64(Id,imagem_b64) VALUES ('%d','%s')"%(id_imagem,imagem)

    cursor.execute(sql)
    con.commit()
    con.close()

site.register(PlanoDeFundo,PlanoDeFundoAdmin)

