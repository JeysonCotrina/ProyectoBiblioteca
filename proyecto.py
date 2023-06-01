import mysql.connector

class Biblioteca():
    def __init__(self):
        self.conexion= mysql.connector.connect(host='localhost',user='root',password='',database='prestamos')

    """def __str__(self):
        datos = self.consulta_usuario()
        aux = ''
        for columna in datos:
            aux += str(columna) + '\n' 
        return aux
    
    def consulta_usuario(self):
        cur=self.conexion.cursor
        sql=f"SELECT * FROM usuario"
        cur.execute(sql)
        datos=cur.fetchall()
        cur.close()
        return datos"""

    def identificar(self,rut_usuario):
        cur=self.conexion.cursor()
        cur.execute(f"""select id_tipo from usuario where rut_usuario ='{rut_usuario}';""")
        n = cur.fetchone()
        cur.execute(f"""select nombre from usuario where rut_usuario ='{rut_usuario}';""")
        o = cur.fetchone()
        while n != None:
            j, = n
            w, = o
            return j,w
