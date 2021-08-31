-- crear una base de datos llamada empresa
-- gestion de los empleados de una empresa, en la cual esta distribuida
-- por departamento (informatica, publicidad, marketing, finanzas)
-- ademas se requiere controlar al personal (nombre, apellido, id) cada
-- personal puede pertenecer a un departamento.alter
-- nota: no todos los empleados tienen departamento

-- un personal a la vez puede ser superior de otro personal
create database empresa;
use empresa;

create table departamentos(
	id int not null auto_increment primary key,
    nombre varchar(30)
);


create table personales(
    id int primary key not null auto_increment,
    identificador text,
    nombre varchar(40),
    apellido varchar(40),
    departamento_id int,
    foreign key (departamento_id) references departamentos(id),
    foreign key (supervisor_id) references personales(id)
);

-- agrega lo que no hayas agregado antes de ejecutar
alter table personales add column supervisor_id int;

alter table personales add foreign key(supervisor_id) references personales(id);