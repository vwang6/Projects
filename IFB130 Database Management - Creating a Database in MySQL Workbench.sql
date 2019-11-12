DROP DATABASE IF EXISTS Oktomook;
CREATE DATABASE Oktomook;

SET FOREIGN_KEY_CHECKS= 0;

DROP TABLE IF EXISTS Customers; 
CREATE TABLE Customers(
       customerNo INT NOT NULL,
	   firstname VARCHAR (15),
       lastName VARCHAR (15),
       address VARCHAR (30),
       city VARCHAR (12),
       state ENUM ('QLD', 'VIC', 'NSW', 'WA', 'TAS', 'NT', 'SA'),
       postcode CHAR (4),
       region VARCHAR (11),
       email VARCHAR (255),
       PRIMARY KEY (customerNo)
);

DROP TABLE IF EXISTS Books; 
CREATE TABLE Books(
	   ISBN CHAR(13) NOT NULL,
       title VARCHAR (30) NOT NULL,
       pubDate DATE,
       PubID INT,
       Cost DECIMAL (13,2),
       Retail VARCHAR (11),
       Discount DECIMAL (13,2),
       category ENUM ('Fitness', 'Children', 'Computer', 'Cooking', 'Business', 'Literature'),
       PRIMARY KEY (ISBN),
       FOREIGN KEY (pubID) REFERENCES Publishers (pubId)
);

DROP TABLE IF EXISTS Orders;
CREATE TABLE Orders(
	   orderNo INT NOT NULL,
       customerNo INT,
       orderDate DATE,
       shipDate DATE,
       street VARCHAR (13),
       city VARCHAR (12),
       state ENUM ('QLD', 'VIC', 'NSW', 'WA', 'TAS', 'NT', 'SA'),
       postcode CHAR (4),
       shipCost DECIMAL (13,2), 
       PRIMARY KEY (orderNo),
       FOREIGN KEY (orderNo) REFERENCES OrdersItems (orderNo),
       FOREIGN KEY (customerNo) REFERENCES Customers (customerNo)
);

DROP TABLE IF EXISTS OrdersItems;
CREATE TABLE OrdersItems(
       orderNo INT NOT NULL,
       itemNo INT,
       ISBN CHAR (13), 
       quantity INT DEFAULT '1',
       paidEach DECIMAL (13,2),
       PRIMARY KEY (orderNo)
);

DROP TABLE IF EXISTS Author;
CREATE TABLE Author(
       authorID INT NOT NULL,
       firstName VARCHAR (15),
       lastName VARCHAR (15),
       PRIMARY KEY (authorID)
);

DROP TABLE IF EXISTS Wrote;
CREATE TABLE Wrote(
       ISBN CHAR (13) NOT NULL, 
       authorID INT NOT NULL,
       PRIMARY KEY (ISBN, authorID), 
       FOREIGN KEY (ISBN) REFERENCES Books (ISBN),
       FOREIGN KEY (authorID) REFERENCES Author (authorID) 
);

DROP TABLE IF EXISTS Publishers;
CREATE TABLE Publishers(
	   pubId INT NOT NULL,
       name VARCHAR (25) NOT NULL, 
       contact VARCHAR (15),
       phoneNo VARCHAR (15),
       PRIMARY KEY (pubId) 
);




       

       
       
	
       
       
       
       
       