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
    list_display = ['nome_fantasia','data_cadastro','logo']

    """Metodo declarado para criar miniatura da imagem depois de salvar"""
    def save_model(self, request, obj, form, change):
        super(EmpresaAdmin, self).save_model(request, obj, form, change)

        if 'foto' in form.changed_data:
            extensao = obj.foto.name.split('.')[-1]
            obj.thumbnail = 'logo/thumbnail/%s.%s'%(obj.id, extensao)
            miniatura = Image.open(obj.foto.path)
            miniatura.thumbnail((100,100), Image.ANTIALIAS)
            miniatura.save(obj.thumbnail.path)

            obj.save()
            read_logo(obj.id)

def read_logo(id_imagem):
#    CREATE TABLE IF NOT EXISTS logo_empresa(Id INT PRIMARY KEY, imagem LONGBLOB);
#    UPDATE empresa SET imagem_b64 = imagem WHERE ID =
    #fin = open("public\\media\\logo\\thumbnail\\"+str(id_imagem)+".jpg","rb")
    fin = open("public/media/logo/thumbnail/"+str(id_imagem)+".jpg","rb")
#    img = fin.read()
    image = base64.b64encode(fin.read())
    con = MySQLdb.connect("localhost","root","","cardapio_web" )
    cursor = con.cursor()
    imagem = "data:image/jpg;base64,%s" % image
    sql = "UPDATE empresa SET imagem_b64 = "%(1,imagem)
    #sql = "INSERT INTO logo_empresa(Id,imagem) VALUES ('%d','%s')"%(1,imagem)
    #sql = "UPDATE empresa SET imagem_b64 = imagem WHERE ID = "%(1,imagem)
#    print sql
#    con = MySQLdb.connect("localhost","root","","cardapio" )

    cursor.execute (sql)
    con.commit()
    con.close()

site.register(Empresa,EmpresaAdmin)

