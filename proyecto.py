import mysql.connector
class Biblioteca():
    def __init__(self):
        self.conexion= mysql.connector.connect(host='localhost',user='root',password='',database='prestamos')
    
    def InfoCliente(self,rut_cliente):
        cur=self.conexion.cursor()
        cur.execute(f"SELECT contrasena,nombre,apellido,telefono,correo,multas,id_tipo_cliente,id_cliente FROM cliente WHERE rut = '{rut_cliente}'")
        datos=cur.fetchone()
        return datos
    
    def Prestamo(self,f_prestamo,f_entrega_acordada,id_cliente,codigo,id_usuario):
        cur=self.conexion.cursor()
        cur.execute(f'INSERT INTO prestamo(f_prestamo,f_entrega_acordada,id_cliente,codigo,id_usuario) VALUES ({f_prestamo},{f_entrega_acordada},{id_cliente},{codigo},{id_usuario})')
        cur.fetchone()

    def BusquedaLibro(self,codigo):
        cur=self.conexion.cursor()
        cur.execute(f'SELECT titulo FROM libro WHERE codigo = "{codigo}" ')
        datos=cur.fetchall()
        return datos
    
    def ValidarPrestamo(self,id_cliente,codigo):
        cur=self.conexion.cursor()
        cur.execute(f'SELECT f_prestamo FROM prestamo WHERE id_cliente = {id_cliente} and codigo = "{codigo}"')
        datos=cur.fetchone()
        return datos
    
    def InfoLibro(self,codigo_libro):
        cur=self.conexion.cursor()
        cur.execute(f"SELECT titulo,cant_ejemplar,autor,editorial,categoria FROM libro WHERE codigo = '{codigo_libro}'")
        datos=cur.fetchone()
        return datos
    
    def ModificarStock(self,codigo_libro):
        cantidad = int(input("ingrese la cantidad a actualizar: "))
        cur=self.conexion.cursor()
        cur.execute(f"UPDATE libro set cant_ejemplar =  {cantidad} WHERE codigo = '{codigo_libro}' ")
        self.conexion.commit()

    def EliminarLibro(self, codigo_libro):
        cur=self.conexion.cursor()
        cur.execute(f"DELETE FROM libro  where codigo = '{codigo_libro}'")
        self.conexion.commit()

    def identificar_Libros(self, codigo_libro):
        cur = self.conexion.cursor()
        cur.execute(f"""select codigo from libro where codigo = '{codigo_libro}' ; """)
        datos = cur.fetchall()
        return datos
    
    def identificar_prestamo(self,codigo_libro):
        cur = self.conexion.cursor()
        cur.execute(f"""SELECT codigo from prestamo where codigo = '{codigo_libro}' ; """)
        datos = cur.fetchall()
        return datos
    
class Encargado(Biblioteca):
    def identificar_usuario(self,rut,contrasena):
        cur=self.conexion.cursor()
        cur.execute(f"""select id_usuario,rut from usuario where rut ='{rut}' and contrasena ='{contrasena}';""")
        datos=cur.fetchone()
        return datos

class Docente(Biblioteca):
    def identificar_docente(self,rut,contrasena):
        cur=self.conexion.cursor()
        cur.execute(f"""select id_cliente,rut,id_tipo_cliente,contrasena from cliente where rut ='{rut}' and id_tipo_cliente={1} and contrasena ='{contrasena}';""")
        datos=cur.fetchall()
        return datos
    
    def datos_docente(self,rut):
        cur=self.conexion.cursor()
        cur.execute(f"""select id_cliente,rut,id_tipo_cliente,contrasena from cliente where rut ='{rut}';""")
        datos=cur.fetchall()
        return datos

class Alumno(Biblioteca):
    def identificar_alumno(self,rut,contrasena):
        cur=self.conexion.cursor()
        cur.execute(f"""select rut,id_tipo_cliente,multas from cliente where rut ='{rut}' and id_tipo_cliente={2} and contrasena ='{contrasena}';""")
        datos=cur.fetchone()
        return datos
