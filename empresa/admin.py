#coding=utf8
try:
    import Image
except ImportError:
    from PIL import Image

from django.contrib.admin import ModelAdmin,site
from empresa.models import Empresa

import base64
import MySQLdb

class EmpresaAdmin(ModelAdmin):
    list_display                    = ['logo','nome_fantasia','data_cadastro']
    list_filter                     = ['nome_fantasia']

    """Metodo declarado para criar miniatura da imagem depois de salvar"""
    def save_model(self, request, obj, form, change):
        super(EmpresaAdmin, self).save_model(request, obj, form, change)

        if 'foto' in form.changed_data:
            extensao = obj.foto.name.split('.')[-1]
            obj.thumbnail = 'logo_empresa/thumbnail/%s.%s'%(obj.id, extensao)
            miniatura = Image.open(obj.foto.path)
            miniatura.thumbnail((100,100), Image.ANTIALIAS)
            miniatura.save(obj.thumbnail.path)

            obj.save()
            insert_logo(obj.id,extensao)

def insert_logo(id_imagem,extensao):
    fin = open("public/media/logo_empresa/thumbnail/"+str(id_imagem)+"."+extensao,"rb")
    print fin
    image = base64.b64encode(fin.read())
    imagem = "data:image/jpg;base64,%s" % image
    con = MySQLdb.connect("localhost","root","","cardapio_web")
    cursor = con.cursor()
    sqlImagesb64 = "DELETE FROM empresa_empresalogob64"
    cursor.execute(sqlImagesb64)
    sql = "INSERT INTO empresa_empresalogob64(Id,imagem_b64) VALUES ('%d','%s')"%(id_imagem,imagem)

    cursor.execute(sql)
    con.commit()
    con.close()

site.register(Empresa,EmpresaAdmin)

