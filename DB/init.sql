CREATE DATABASE IF NOT EXISTS flaskdb;

USE flaskdb;

CREATE TABLE IF NOT EXISTS usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(50) NOT NULL
);

INSERT INTO usuarios (username, password) VALUES ('admin', '1234');