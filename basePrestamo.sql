create database prestamos;
use prestamos;

CREATE TABLE usuario(
id_usuario int primary key auto_increment,
rut varchar(10),
contrasena varchar(100),
nombre varchar(50),
apellido varchar(50),
telefono int(9),
correo varchar(50)
);

CREATE TABLE libro(
codigo varchar(5) primary key,
titulo varchar(50),
cant_ejemplar int,
autor varchar(50),
editorial varchar(50),
categoria varchar(50)
);

create table tipo_cliente(
id_tipo_cliente int primary key auto_increment,
nombre varchar(15)
);

create table cliente (
id_cliente int primary key auto_increment,
rut varchar(10),
contrasena varchar(100),
nombre varchar(50),
apellido varchar(50),
telefono int(9),
correo varchar(50),
multas int,
id_tipo_cliente int,
constraint fk_id_tipo_cliente foreign key (id_tipo_cliente) references tipo_cliente (id_tipo_cliente)
);

CREATE TABLE estado_prestamo(
id_estado int primary key auto_increment,
nombre varchar(50)
);

CREATE TABLE prestamo(
id_prestamo int primary key auto_increment,
f_prestamo date,
f_entrega_acordada date,
id_cliente int,
codigo varchar(5),
id_usuario int,
constraint fk_id_cliente foreign key (id_cliente) references cliente (id_cliente),
constraint fk_codigo foreign key (codigo) references libro(codigo),
constraint fk_id_usuario foreign key (id_usuario) references usuario (id_usuario)
);

CREATE TABLE prestamo_libro(
id_prestamo_libro int,
f_real_entrega date,
id_estado int,
multa int,
id_prestamo int,
constraint fk_id_estado foreign key (id_estado) references estado_prestamo (id_estado),
constraint fk_id_prestamo foreign key (id_prestamo) references prestamo (id_prestamo)
);

-- ingreso de Usuarios
INSERT INTO usuario(rut,contrasena,nombre,apellido,telefono,correo) 
VALUES('21475689-7','juan222','Juan','Roldan',965487721,'juan123@gmail.com');
INSERT INTO usuario(rut,contrasena,nombre,apellido,telefono,correo) 
VALUES('24785213-1','piero222','Piero','Huaman',954871236,'piero25@gmail.com');
INSERT INTO usuario(rut,contrasena,nombre,apellido,telefono,correo) 
VALUES('25745816-4','jazmin222','Jazmin','Cueva',941255299,'jazmin244@hotmail.com');
SELECT * FROM Usuario;

-- ingreso de Tipo de cliente
INSERT INTO tipo_cliente(nombre) VALUES('Docente');
INSERT INTO tipo_cliente(nombre) VALUES('Alumno');
SELECT * FROM tipo_cliente;

-- ingreso de Cliente
SELECT * FROM cliente;
INSERT INTO  cliente(rut,contrasena,nombre,apellido,telefono,correo,id_tipo_cliente,multas) 
VALUES ('16547825-4','raul222','Raul','Rodriguez',964251872,'raul34@gmail.com',1,0);
INSERT INTO  cliente(rut,contrasena,nombre,apellido,telefono,correo,id_tipo_cliente,multas) 
VALUES ('25485221-2','elvira222','Elvira','Yraita',922411455,'elvira23@gamil.com',1,0);
INSERT INTO  cliente(rut,contrasena,nombre,apellido,telefono,correo,id_tipo_cliente,multas) 
VALUES ('19655124-1','justina222','Justina','Mejilla',912355354,'justina.4@hotmail.com',1,0);
INSERT INTO  cliente(rut,contrasena,nombre,apellido,telefono,correo,id_tipo_cliente,multas) 
VALUES ('19551123-5','gabriel222','Gabriel','Zavaleta',966244445,'gabriel0@gamil.com',2,0);
INSERT INTO  cliente(rut,contrasena,nombre,apellido,telefono,correo,id_tipo_cliente,multas) 
VALUES ('22552145-2','ana222','Ana','Villacorta',954315636,'ana.v@hotmail.com',2,0);
INSERT INTO  cliente(rut,contrasena,nombre,apellido,telefono,correo,id_tipo_cliente,multas) 
VALUES ('25114554-3','maximo222','Maximo','Ulloa',965418713,'max_ulloa@gamil.com',2,0);


-- ingreso de estado_prestamo
SELECT * FROM estado_prestamo;
INSERT INTO  estado_prestamo(nombre) VALUES ('Entregado');
INSERT INTO  estado_prestamo(nombre) VALUES ('Retardado');

-- ingreso de Libros
INSERT INTO libro(codigo,titulo,cant_ejemplar,autor,editorial,categoria) 
VALUES('A19SD','Tu mejor amigo',5,'W.Bruce Cameron','Roca Bolsillo','Novela');
INSERT INTO libro(codigo,titulo,cant_ejemplar,autor,editorial,categoria) 
VALUES('A20SD','Vivir De Las Redes',7,'Sergio Barreda Coy','Alienta Editorial','Relaciones Públicas');
INSERT INTO libro(codigo,titulo,cant_ejemplar,autor,editorial,categoria) 
VALUES('A21SD','El Economista Callejero',5,'Axel Kaiser','Ediciones El Mercurio','Economia Politica');
INSERT INTO libro(codigo,titulo,cant_ejemplar,autor,editorial,categoria) 
VALUES('A22SD','La bolsa o la vida',2,'Vicki Robin y Joe Dominguez','Kitsune Books','Gestion Empresarial');
INSERT INTO libro(codigo,titulo,cant_ejemplar,autor,editorial,categoria) 
VALUES('A23SD','Tecnologia y Narrativa Audivisual',10,'Javier Sierra Sanchez','Fragua','Estudio de Comunicacion');
INSERT INTO libro(codigo,titulo,cant_ejemplar,autor,editorial,categoria) 
VALUES('A24SD','Python paso a paso',9,'Pablo Hinojosa Guti','Ediciones de la U','Libro sobre informatica');
INSERT INTO libro(codigo,titulo,cant_ejemplar,autor,editorial,categoria) 
VALUES('A25SD','Marta Peirano',7,'Contra el futuro','Debate','Tecnologia de la Informacion');
INSERT INTO libro(codigo,titulo,cant_ejemplar,autor,editorial,categoria) 
VALUES('A26SD','Luna',4,'Jose Maria Sancho','Planeta','Astronomia');
INSERT INTO libro(codigo,titulo,cant_ejemplar,autor,editorial,categoria) 
VALUES('A27SD','Neurociencia del cuerpo',3,'Nazareth Perales Castellano','Kairos','Neurociencias');
INSERT INTO libro(codigo,titulo,cant_ejemplar,autor,editorial,categoria) 
VALUES('A28SD','Culpa Mia',8,'Mercedes Ron','Montena','Ficcion Infantil y Juvenil: Romantica');
INSERT INTO libro(codigo,titulo,cant_ejemplar,autor,editorial,categoria) 
VALUES('A29SD','De Sangre y Cenizas',12,'Jennifer L.Armentrout','Puck','Calificadores De Interes');
SELECT * FROM libro;
-- PRESTAMO
INSERT INTO prestamo(f_prestamo,f_entrega_acordada,id_cliente,codigo,id_usuario)
VALUES('2023-06-15','2023-06-18',3,'A27SD',1);

SELECT * FROM prestamo;

-- PRESTAMO_LIBRO
INSERT INTO prestamo_libro(f_real_entrega,id_estado,multa,id_prestamo)
VALUES('2023-06-19',1,1000,1);

SELECT*FROM prestamo_libro;
