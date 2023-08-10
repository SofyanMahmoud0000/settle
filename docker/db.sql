CREATE DATABASE IF NOT EXISTS settle;

use settle;

CREATE TABLE IF NOT EXISTS books (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    price float NOT NULL,
    release_date date,
    category varchar(255)
);

CREATE TABLE IF NOT EXISTS authors (
	id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name varchar(255) NOT NULL,
	birthday date
);

CREATE TABLE IF NOT EXISTS book_authors (
	book_id int,
	author_id int,
	PRIMARY KEY (book_id, author_id),
	FOREIGN KEY (book_id) REFERENCES books(id),
  FOREIGN KEY (author_id) REFERENCES authors(id)
);

CREATE TABLE IF NOT EXISTS users (
	id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name varchar(255) NOT NULL,
	username varchar(255) NOT NULL UNIQUE,
	password varchar(255) NOT NULL
);