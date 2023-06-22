import mysql.connector

class Biblioteca():
    def __init__(self):
        self.conexion= mysql.connector.connect(host='localhost',user='root',password='',database='prestamos')

    
    def identificar_usuario(self,rut,contrasena):
        cur=self.conexion.cursor()
        cur.execute(f"""select rut from usuario where rut ='{rut}' and contrasena ='{contrasena}';""")
        datos=cur.fetchall()
        return datos
    
    def identificar_docente(self,rut,contrasena):
        cur=self.conexion.cursor()
        cur.execute(f"""select rut,id_tipo_cliente,contrasena from cliente where rut ='{rut}' and id_tipo_cliente={1} and contrasena ='{contrasena}';""")
        datos=cur.fetchall()
        return datos
    
    def identificar_alumno(self,rut,contrasena):
        cur=self.conexion.cursor()
        cur.execute(f"""select rut,id_tipo_cliente from cliente where rut ='{rut}' and id_tipo_cliente={2} and contrasena ='{contrasena}';""")
        datos=cur.fetchall()
        return datos
