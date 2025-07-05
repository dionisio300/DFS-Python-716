create database eventos;
use eventos;

create table evento (
id int primary key auto_increment,
nome varchar(100),
data_evento date not null,
local_Evento varchar(100) not null,
hora time not null,
lotacao int not null,
ingressos_vendidos int not null,
ingressos_disponiveis int not null
);

insert into evento (nome,data_evento,local_Evento,hora,lotacao,ingressos_vendidos,ingressos_disponiveis) values
('Show de Rock','2025-08-06','Estádio','21:00',3000,2000,1000);

select * from evento;

insert into evento (nome,data_evento,local_Evento,hora,lotacao,ingressos_vendidos,ingressos_disponiveis) values
('Show do Djavan','2025-08-10','Teatro','22:00',2000,1000,1000),
('Show da Pitty','2025-10-10','Praia','22:00',5000,1000,4000);

select * from evento;

update evento set 
nome = 'Show de MPB',
data_evento = '2025-09-09',
local_Evento = 'Praia', 
hora = '22:00:00',
lotacao = 10000,
ingressos_vendidos = 3000,
ingressos_disponiveis = 7000 where id = 1;

delete from evento where id = 1;
select * from evento;

create table usuarios (
id int primary key auto_increment,
nome varchar(100) not null,
email varchar(100) unique not null,
senha varchar(100) not null,
tipo enum('admin', 'cliente')
);

insert into usuarios (nome, email, senha, tipo) values 
('João','joao@mail.com','
','cliente'),
('Maria','maria@mail.com','456','admin'),
('Caio','caio@mail.com','789','cliente'),
('Leticia','leticia@mail.com','987','admin');

select * from usuarios;



