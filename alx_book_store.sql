CREATE DATABASE IF NOT EXISTS alx_book_store;

USE alx_book_store;

CREATE TABLE Authors (
    author_id int PRIMARY KEY auto_increment,
    author_name varchar(215) not null
);

CREATE TABLE Books (
    book_id int PRIMARY KEY auto_increment,
    book_title varchar(130) not null,
    author_id int,
    publication_date date,
    price DOUBLE not null,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

CREATE TABLE Customers (
    customer_id int PRIMARY KEY auto_increment,
    customer_name VARCHAR(215) not null,
    email VARCHAR(215) unique not null,
    address TEXT
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Order_Details (
    orderdetail_id INT AUTO AUTO_INCREMENT,
    order_id INT,
    book_id INT,
    quantity DOUBLE NOT NULL,
    PRIMARY KEY (orderdetail_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)     
);
