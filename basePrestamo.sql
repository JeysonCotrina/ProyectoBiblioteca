create database prestamos;
use prestamos;

CREATE TABLE usuario(
rut_usuario varchar(10) primary key,
contrasena_usuario varchar(100),
nombre_usuario varchar(50),
apellido_usuario varchar(50),
telefono_usuario int(9),
correo_usuario varchar(50)
);

CREATE TABLE libro(
codigo_libro varchar(5) primary key,
titulo_libro varchar(50),
cant_ejemplar int,
autor varchar(50),
editorial varchar(50),
categoria varchar(50)
);

create table tipo_cliente(
id_tipo_cliente int primary key auto_increment,
nombre_tipo varchar(15)
);

create table cliente (
rut_cliente varchar(10) primary key,
contrasena_cliente varchar(100),
nombre_cliente varchar(50),
apellido_cliente varchar(50),
telefono_cliente int(9),
correo_cliente varchar(50),
id_tipo_cliente int,
constraint fk_id_tipo_cliente foreign key (id_tipo_cliente) references tipo_cliente (id_tipo_cliente)
);

CREATE TABLE estado_prestamo(
id_estado int primary key auto_increment,
nombre_estado varchar(50)
);

CREATE TABLE prestamo_libro(
id_prestado_libro int primary key auto_increment,
f_prestamo date,
f_entrega date,
f_devolucion date,
multa int,
rut_cliente varchar(10),
codigo_libro varchar(5),
rut_usuario varchar(10),
id_estado int,
constraint fk_rut_cliente foreign key (rut_cliente) references cliente (rut_cliente),
constraint fk_codigo_libro foreign key (codigo_libro) references libro (codigo_libro),
constraint fk_rut_usuario foreign key (rut_usuario) references usuario (rut_usuario),
constraint fk_id_estado foreign key (id_estado) references estado_prestamo(id_estado)
);

CREATE TABLE reporte_prestamo(
id_reporte int primary key auto_increment,
id_prestado_libro int,
constraint fk_id_prestado_libro foreign key (id_prestado_libro) references prestamo_libro(id_prestado_libro)
);
-- ingreso de Usuarios
INSERT INTO usuario(rut_usuario,contrasena_usuario,nombre_usuario,apellido_usuario,telefono_usuario,correo_usuario) 
VALUES('21475689-7','juan222','Juan','Roldan',965487721,'juan123@gmail.com');
INSERT INTO usuario(rut_usuario,contrasena_usuario,nombre_usuario,apellido_usuario,telefono_usuario,correo_usuario) 
VALUES('24785213-1','piero222','Piero','Huaman',954871236,'piero25@gmail.com');
INSERT INTO usuario(rut_usuario,contrasena_usuario,nombre_usuario,apellido_usuario,telefono_usuario,correo_usuario) 
VALUES('25745816-4','jazmin222','Jazmin','Cueva',941255299,'jazmin244@hotmail.com');
SELECT * FROM Usuario;

-- ingreso de Tipo de cliente
INSERT INTO tipo_cliente(nombre_tipo) VALUES('Docente');
INSERT INTO tipo_cliente(nombre_tipo) VALUES('Alumno');
SELECT * FROM tipo_cliente;

-- ingreso de Cliente
SELECT * FROM cliente;
INSERT INTO  cliente(rut_cliente,contrasena_cliente,nombre_cliente,apellido_cliente,telefono_cliente,correo_cliente,id_tipo_cliente) 
VALUES ('16547825-4','raul222','Raul','Rodriguez',964251872,'raul34@gmail.com',1);
INSERT INTO  cliente(rut_cliente,contrasena_cliente,nombre_cliente,apellido_cliente,telefono_cliente,correo_cliente,id_tipo_cliente) 
VALUES ('25485221-2','elvira222','Elvira','Yraita',922411455,'elvira23@gamil.com',1);
INSERT INTO  cliente(rut_cliente,contrasena_cliente,nombre_cliente,apellido_cliente,telefono_cliente,correo_cliente,id_tipo_cliente) 
VALUES ('19655124-1','justina222','Justina','Mejilla',912355354,'justina.4@hotmail.com',1);
INSERT INTO  cliente(rut_cliente,contrasena_cliente,nombre_cliente,apellido_cliente,telefono_cliente,correo_cliente,id_tipo_cliente) 
VALUES ('19551123-5','gabriel222','Gabriel','Zavaleta',966244445,'gabriel0@gamil.com',2);
INSERT INTO  cliente(rut_cliente,contrasena_cliente,nombre_cliente,apellido_cliente,telefono_cliente,correo_cliente,id_tipo_cliente) 
VALUES ('22552145-2','ana222','Ana','Villacorta',954315636,'ana.v@hotmail.com',2);
INSERT INTO  cliente(rut_cliente,contrasena_cliente,nombre_cliente,apellido_cliente,telefono_cliente,correo_cliente,id_tipo_cliente) 
VALUES ('25114554-3','maximo222','Maximo','Ulloa',965418713,'max_ulloa@gamil.com',2);


-- ingreso de estado_prestamo
SELECT * FROM estado_prestamo;
INSERT INTO  estado_prestamo(nombre_estado) VALUES ('entregado');
INSERT INTO  estado_prestamo(nombre_estado) VALUES ('retardado');

-- ingreso de Libros
INSERT INTO libro(codigo_libro,titulo_libro,cant_ejemplar,autor,editorial,categoria) 
VALUES('A19SD','Tu mejor amigo',5,'W.Bruce Cameron','Roca Bolsillo','Novela');
INSERT INTO libro(codigo_libro,titulo_libro,cant_ejemplar,autor,editorial,categoria) 
VALUES('A20SD','Vivir De Las Redes',7,'Sergio Barreda Coy','Alienta Editorial','Relaciones Públicas');
INSERT INTO libro(codigo_libro,titulo_libro,cant_ejemplar,autor,editorial,categoria) 
VALUES('A21SD','El Economista Callejero',5,'Axel Kaiser','Ediciones El Mercurio','Economia Politica');
INSERT INTO libro(codigo_libro,titulo_libro,cant_ejemplar,autor,editorial,categoria) 
VALUES('A22SD','La bolsa o la vida',2,'Vicki Robin y Joe Dominguez','Kitsune Books','Gestion Empresarial');
INSERT INTO libro(codigo_libro,titulo_libro,cant_ejemplar,autor,editorial,categoria) 
VALUES('A23SD','Tecnologia y Narrativa Audivisual',10,'Javier Sierra Sanchez','Fragua','Estudio de Comunicacion');
INSERT INTO libro(codigo_libro,titulo_libro,cant_ejemplar,autor,editorial,categoria) 
VALUES('A24SD','Python paso a paso',9,'Pablo Hinojosa Guti','Ediciones de la U','Libro sobre informatica');
INSERT INTO libro(codigo_libro,titulo_libro,cant_ejemplar,autor,editorial,categoria) 
VALUES('A25SD','Marta Peirano',7,'Contra el futuro','Debate','Tecnologia de la Informacion');
INSERT INTO libro(codigo_libro,titulo_libro,cant_ejemplar,autor,editorial,categoria) 
VALUES('A26SD','Luna',4,'Jose Maria Sancho','Planeta','Astronomia');
INSERT INTO libro(codigo_libro,titulo_libro,cant_ejemplar,autor,editorial,categoria) 
VALUES('A27SD','Neurociencia del cuerpo',3,'Nazareth Perales Castellano','Kairos','Neurociencias');
INSERT INTO libro(codigo_libro,titulo_libro,cant_ejemplar,autor,editorial,categoria) 
VALUES('A28SD','Culpa Mia',8,'Mercedes Ron','Montena','Ficcion Infantil y Juvenil: Romantica');
INSERT INTO libro(codigo_libro,titulo_libro,cant_ejemplar,autor,editorial,categoria) 
VALUES('A29SD','De Sangre y Cenizas',12,'Jennifer L.Armentrout','Puck','Calificadores De Interes');
SELECT * FROM libro;

-- ingreso de prestamo_libro (agregar más datos mediante python)
SELECT * FROM prestamo_libro;
INSERT INTO  prestamo_libro() VALUES();
-- ingreso de reporte_prestamo (agregar mas datos mediante python)
SELECT * FROM reporte_prestamo; 
INSERT INTO  reporte_prestamo() VALUES();
