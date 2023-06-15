import mysql.connector

class Biblioteca():
    def __init__(self):
        self.conexion= mysql.connector.connect(host='localhost',user='root',password='',database='prestamos')

    def __str__(self):
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
        return datos

    def identificar_usuario(self,rut,contrasena):
        cur=self.conexion.cursor()
        cur.execute(f"""select rut_usuario from usuario where rut_usuario ='{rut}' and contrasena_usuario ='{contrasena}';""")
        datos=cur.fetchall()
        return datos
    
    def identificar_docente(self,rut,contrasena):
        cur=self.conexion.cursor()
        cur.execute(f"""select rut_cliente,id_tipo_cliente,contrasena_cliente from cliente where rut_cliente ='{rut}' and id_tipo_cliente={1} and contrasena_cliente ='{contrasena}';""")
        datos=cur.fetchall()
        return datos
    
    def identificar_alumno(self,rut,contrasena):
        cur=self.conexion.cursor()
        cur.execute(f"""select cliente.rut_cliente,cliente.id_tipo_cliente from cliente where rut_cliente ='{rut}' and id_tipo_cliente={2} and contrasena_cliente ='{contrasena}';""")
        datos=cur.fetchall()
        return datos
