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

INSERT INTO users(name, username, password) VALUES('Admin', 'admin', 'password');

INSERT INTO authors(name, birthday) VALUES('Gayle Laakmann McDowell', '1998-02-21');
INSERT INTO authors(name, birthday) VALUES('James Turnbull', '1998-02-21');
INSERT INTO authors(name, birthday) VALUES('Kathy Sierra', '1998-02-21');
INSERT INTO authors(name, birthday) VALUES('Robert Cecil Martin', '1998-02-21');
INSERT INTO authors(name, birthday) VALUES('Ben Straub', '1998-02-21');


INSERT INTO books(name, price, release_date, category) 
VALUES('Clean Code', 240, '2008-08-01','Programming');

INSERT INTO books(name, price, release_date, category) 
VALUES('Head First Design Pattern', 300, '2004-10-01','OOP');

INSERT INTO books(name, price, release_date, category) 
VALUES('Pro Git', 240, '2009-08-26','VCS');

INSERT INTO books(name, price, release_date, category) 
VALUES('The Docker Book', 280, '2014-01-01','DepOps');

INSERT INTO books(name, price, release_date, category) 
VALUES('Cracking Coding Interview', 350, '2089-01-01','Problem solving');



INSERT INTO book_authors(book_id, author_id) VALUES(1, 4);
INSERT INTO book_authors(book_id, author_id) VALUES(2, 3);
INSERT INTO book_authors(book_id, author_id) VALUES(3, 5);
INSERT INTO book_authors(book_id, author_id) VALUES(4, 2);
INSERT INTO book_authors(book_id, author_id) VALUES(5, 1);
