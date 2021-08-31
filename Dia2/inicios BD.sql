-- Esto es un comentario

create database pruebas;

-- para indicar que BD voy a utilizar 
USE pruebas;

create table personas(
    -- ahora definiremos las columnas de la tabla personas
    -- las llaves primarias (primary key) siempre deben ser UNICAS E IRREPETIBLES
    -- nombre_col tipo_dato [ primary key | not null ]
    id int primary key not null auto_increment,
    -- el unique indica que si ingreso un valor, ese valor no se
    -- puede repetir con otro ingresado anteriormente, mas no obliga al usuario
    -- a ingresarlo
    documento varchar(20) unique,
    tipo_documento enum('DNI','C.E','PASAPORTE','S/ DOCUMENTO'),
    nombre varchar(25),
    apellido varchar(50),
    correo varchar(100) unique,
    sexo enum('FEMENINO','MASCULINO','OTRO') not null,
    fecha_nacimiento date
);

insert into personas (documento, tipo_documento, nombre, apellido, correo, fecha_nacimiento, sexo)
values               ('73500741','DNI','CARLOS','CASTRO','carlos.castro@gmail.com','1989-08-04','Masculino');

-- FORMA DE VISUALIZAR LOS DATOS DE UNA TABLA INDICANDO LAS COLUMNAS
select documento, nombre, fecha_nacimiento from personas;

-- FORMA DE VISUALIZAR TODAS LAS COLUMNAS DE UNA TABLA
select * from personas;

insert into personas (documento, tipo_documento, nombre, apellido, correo, fecha_nacimiento, sexo)
values               ('12345678','C.E','MARIA','PERÉZ','m.perez@gmail.com','1995-12-10','Femenino');

insert into personas (documento, tipo_documento, nombre, apellido, correo, fecha_nacimiento, sexo)
values               ('12345679','C.E','JOSE','NUÑEZ','J.NUÑEZ@gmail.com','1999-11-10','Femenino');

insert into personas (documento, tipo_documento, nombre, apellido, correo, fecha_nacimiento, sexo)
values               ('56781234','C.E','MARIELA','MIRANDA','m.miranda@gmail.com','2000-02-19','Femenino');

-- ctrl + enter señalando con el cursor para que se pueda ejecutar

-- Modificar algunas columnas de la tabla (tiene algunas restricciones si es que ya tengo informacion grabada)
ALTER TABLE personas MODIFY documento varchar(20) unique;

SELECT * FROM personas  WHERE nombre= 'CARLOS' AND sexo = 'MASCULINO';

-- eLIMINAR REGISTRO
DELETE FROM personas WHERE correo = 'J.NUÑEZ@gmail.com';

select * from personas;

-- Actualizar uno o varios registros
UPDATE personas SET nombre = 'RAMIRO' where ID = 1;

CREATE TABLE medicos(
	id int primary key not null auto_increment,
	cmp varchar(5) unique not null, -- colegio médico del Perúcheck
	nombre varchar(30),
    apellido varchar(50)
);

CREATE TABLE historial_vacunaciones(
	id int primary key not null auto_increment,
    vacuna enum('PFISER', 'SINOPHARM', 'ASTRAZENECA'),
    lote varchar(10),
    fecha date,
    medico_id int,
    paciente_id INT,
    -- para crear las relaciones
    foreign key (medico_id) references medicos(id),
    foreign key (paciente_id) references personas(id)
);

insert into medicos (cmp, nombre, apellido)
VALUES               ('1234','RAUL','MUÑOZ'),
                    ('1236','ROSA','HIDALGO'),
                    ('5829','SOFIA','ALEMAN');
                    
INSERT INTO historial_vacunaciones (vacuna, lote, medico_id, paciente_id, fecha) 
VALUES                                ('PFIZER','1234',1, 1, '2021-07-24'),
									  ('PFIZER','1234',2, 2, now()),
                                      ('SINOPHARM', '5948', 3, 6, now());
                                  -- ('SINOPHARM','1598', 2, 2, '2021-08-01'),
                                  --  ('ASTRAZENECA','1959', 1, 6, '2021-08-24'),
                                   
                                   
SELECT * FROM HISTORIAL_VACUNACIONES;

-- DEVOLVER TODOS LOS REGISTROS DE HISTORIALES DE VACUNACION QUE SEAN PFIZER O ASTRAZENECA
SELECT *
FROM historial_vacunaciones
WHERE vacuna = 'PFIZER'
    OR vacuna = 'ASTRAZENECA';
SELECT *
FROM historial_vacunaciones
WHERE vacuna IN ('PFIZER', 'ASTRAZENECA');
-- DELETE FROM HISTORIAL_VACUNACIONES;
-- set SQL_SAFE_UPDATES = 1;