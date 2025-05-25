CREATE DATABASE IF NOT EXISTS usuariosdb;
USE usuariosdb;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

INSERT INTO usuarios (username, password)
VALUES ('admin', '1234');
