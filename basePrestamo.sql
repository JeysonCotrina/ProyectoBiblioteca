create database prestamos;
use prestamos;

create table tipo_usuario(
id_tipo int primary key auto_increment,
nombre varchar(15)
);

create table usuario (
rut_usuario varchar(10) primary key,
id_tipo int,
nombre varchar(50),
apellido varchar(50),
telefono int(9),
correo varchar(50),
constraint fk_id_tipo foreign key (id_tipo) references tipo_usuario (id_tipo)
);

create table libro(
codigo_libro varchar(5) primary key,
cant_ejemplar int,
titulo varchar(50),
autor varchar(50)
);

create table estadoPrestamo(
id_estadoPrestamo int primary key auto_increment,
nombre varchar(10)
);

create table prestamo (
id_prestamo int primary key auto_increment,
codigo_libro varchar(5), -- Libro
rut_usuario varchar(10),
f_entrega date, -- dia en que se tendria que entregar el libro según la fecha establecida
f_prestamo date, -- dia en que se realiza el prestamo
f_devolucion date, -- dia en que el usuario devuelve el libro
multa float,
id_estadoPrestamo int,  -- al fia, retrasado
constraint fk_id_estadoPrestamo foreign key (id_estadoPrestamo) references estadoPrestamo (id_estadoPrestamo),
constraint fk_codigo_libro foreign key (codigo_libro) references libro (codigo_libro),
constraint fk_rut_usuario foreign key (rut_usuario) references usuario (rut_usuario)
);

-- ingresar tipo de usuario
insert into tipo_usuario(nombre) value ('Docente');
insert into tipo_usuario(nombre) value ('Alumno');
insert into tipo_usuario(nombre) value ('Encargado');

SELECT*FROM tipo_usuario;

-- Ingreso de datos docente
insert into usuario(rut_usuario,id_tipo,nombre,apellido,telefono,correo) values ('25009286-3',1,'Piero','Huaman',965630336,'pierohuaman654@gmail.com');
insert into usuario(rut_usuario,id_tipo,nombre,apellido,telefono,correo) values ('23976475-6',1,'Juan','Roldan',992030738,'juanroldan123@gmail.com');
insert into usuario(rut_usuario,id_tipo,nombre,apellido,telefono,correo) values ('19283746-8',1,'Elvira','Yraita',983746237,'elvirayraita23@gmail.com');
insert into usuario(rut_usuario,id_tipo,nombre,apellido,telefono,correo) values ('21908266-0',1,'Britany','Villacorta',939402847,'britanyvillacorta24@gmail.com');
insert into usuario(rut_usuario,id_tipo,nombre,apellido,telefono,correo) values ('22937480-3',1,'Pedro','Zavaleta',992837465,'Pedrozavaleta624@gmail.com');
insert into usuario(rut_usuario,id_tipo,nombre,apellido,telefono,correo) values ('19374827-8',1,'Marlon','Villacorta',982736372,'marlonvillacorta234@gmail.com');
insert into usuario(rut_usuario,id_tipo,nombre,apellido,telefono,correo) values ('18372536-5',1,'Leidy','Zavaleta',927399182,'leidyzavaleta834@gmail.com');
insert into usuario(rut_usuario,id_tipo,nombre,apellido,telefono,correo) values ('29304859-3',1,'Justina','Castillo',993027493,'justinacastillo7867@gmail.com');
insert into usuario(rut_usuario,id_tipo,nombre,apellido,telefono,correo) values ('19203846-2',2,'Gabriel','Polo',922374839,'gabrielpolo543@gmail.com');
insert into usuario(rut_usuario,id_tipo,nombre,apellido,telefono,correo) values ('24837947-1',2,'Veronica','Andrade',928837774,'veronicaandrade354@gmail.com');
insert into usuario(rut_usuario,id_tipo,nombre,apellido,telefono,correo) values ('29273537-7',2,'Aaron','Alarcon',927384492,'aaronalarcon297@gmail.com');
insert into usuario(rut_usuario,id_tipo,nombre,apellido,telefono,correo) values ('29374615-4',2,'Maricielo','Rodriguez',999273812,'maricielorodriguez_483@gmail.com');
insert into usuario(rut_usuario,id_tipo,nombre,apellido,telefono,correo) values ('23647382-2',2,'Zully','Zavaleta',900023417,'zullyzavaleta.324@gmail.com');
insert into usuario(rut_usuario,id_tipo,nombre,apellido,telefono,correo) values ('21273534-5',2,'Renzo','Cardenas',977384829,'renzocardenas.490@gmail.com');
insert into usuario(rut_usuario,id_tipo,nombre,apellido,telefono,correo) values ('23927462-8',2,'Jose','Bellina',928837520,'josebellina_483@gmail.com');
insert into usuario(rut_usuario,id_tipo,nombre,apellido,telefono,correo) values ('23462532-3',2,'Alexis','Soteldo',917384334,'alexissoteldo983@gmail.com');
insert into usuario(rut_usuario,id_tipo,nombre,apellido,telefono,correo) values ('23432532-9',1,'Jerson','Pastor',933748123,'jersonpastor.409@gmail.com');
insert into usuario(rut_usuario,id_tipo,nombre,apellido,telefono,correo) values ('21234753-6',1,'Ernesto','Valles',974833178,'ernestovalles_348@gmail.com');
insert into usuario(rut_usuario,id_tipo,nombre,apellido,telefono,correo) values ('24329483-3',1,'Brigit','Sanchez',982237563,'brigitsanchez.09@gmail.com');
insert into usuario(rut_usuario,id_tipo,nombre,apellido,telefono,correo) values ('24534623-6',3,'Gabriela','Perez',922746399,'gabrielaperez_20@gmail.com');
insert into usuario(rut_usuario,id_tipo,nombre,apellido,telefono,correo) values ('19383723-2',3,'Pablo','Vizlao',927364983,'pablovizlao.29@gmail.com');        

SELECT * FROM usuario;

-- ingresar datos de estado
insert into estadoPrestamo(nombre) value ('al dia');
insert into estadoPrestamo(nombre) value ('en retraso');
SELECT * FROM estadoPrestamo;

-- ingresar datos libros
insert into libro(codigo_libro,cant_ejemplar,titulo,autor) values ('AIS12',10,'Analitica predictiva','Eric Siegel');
insert into libro(codigo_libro,cant_ejemplar,titulo,autor) values ('AIS11',5,'Analisis y diseño de sistemas','Julie E.Kendall');
insert into libro(codigo_libro,cant_ejemplar,titulo,autor) values ('AIS10',2,'El libro negro del programador','Rafael Gómez Blanes');
insert into libro(codigo_libro,cant_ejemplar,titulo,autor) values ('AIS09',8,'El viaje de la humanidad','Oded Galor');
insert into libro(codigo_libro,cant_ejemplar,titulo,autor) values ('AIS08',5,'La teoria del caos','Alberto Perez Izquierdo');
insert into libro(codigo_libro,cant_ejemplar,titulo,autor) values ('AIS07',8,'Mentalidad estratégica','Carlos Niezen');
insert into libro(codigo_libro,cant_ejemplar,titulo,autor) values ('AIS06',11,'El libro que tu cerebro no quiere leer','David del rosario');
insert into libro(codigo_libro,cant_ejemplar,titulo,autor) values ('AIS05',7,'El arte de la invisibilidad','Kevin Mitnick');
insert into libro(codigo_libro,cant_ejemplar,titulo,autor) values ('AIS04',3,'Hacerse el weón','Pablo Riccheri');
SELECT * FROM libro;

select*from prestamo;