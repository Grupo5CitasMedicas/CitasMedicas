CREATE SCHEMA Consultorio;
USE Consultorio;

CREATE TABLE Doctores(
	id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre varchar(20) NOT NULL,
    apellido varchar(20) NOT NULL,
    celular bigint,
    cargo ENUM('Enfermero', 'Cirujano', 'Consultor', 'Residente')
);

CREATE TABLE Pacientes(
	id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre varchar(20) NOT NULL,
    apellido varchar(20) NOT NULL,
    celular bigint,
    direccion varchar(50),
    sedeAtencion varchar(30) NOT NULL,
    estadoCivil ENUM('Soltero', 'Casado', 'Viudo', 'Unión Libre')
);

CREATE TABLE Usuarios(
	id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    user varchar(20) NOT NULL,
    pass varchar(20) NOT NULL,
    rol ENUM('Doctor', 'Paciente')
);

CREATE TABLE Citas(
	id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    fecha datetime,
    idDoctor int,
    idPaciente int,
    tipoConsulta varchar(20),
    comentario varchar(200),
    FOREIGN KEY (idDoctor) REFERENCES Doctores(id),
    FOREIGN KEY (idPaciente) REFERENCES Pacientes(id)
);