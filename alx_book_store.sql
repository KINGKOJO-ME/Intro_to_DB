CREATE DATABASE alx_book_store;

USE alx_book_store;

CREATE TABLE Authors (
    author_id int primary key auto_increment,
    author_name varchar(215) not null,
);

CREATE TABLE Books (
    book_id int primary key auto_increment,
    book_title varchar(130) not null,
    author_id int,
    publication_date date,
    price DOUBLE not null,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

CREATE TABLE Cusstomers (
    customer_id int primary key auto_increment,
    customer_name varchar(215) not null,
    email varchar(215) unique not null,
    address TEXT
);

CREATE TABLE Orders (
    order_id int primary key auto_increment,
    customer_id int,
    order_date date not null,
    FOREIGN KEY (customer_id) REFERENCES Cusstomers(customer_id)
);

CREATE TABLE Order_DEtails (
    orderdetailid int primary key auto_increment,
    order_id int,
    book_id int,
    quantity DOUBLE not null,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);
