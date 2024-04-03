create database project;
use project;
create table product_category(pc_id numeric(10),name varchar(20), description varchar(50), primary key(pc_id));
select * from product_category;
INSERT INTO product_category VALUES ('001', 'Classic Black Pen', 'A sleek black ballpoint pen with smooth ink flow');
INSERT INTO product_category VALUES ('002', 'Floral Notebook', 'A sleek black ballpoint pen with smooth ink flow');
INSERT INTO product_category VALUES ('003', 'Sticky Notes Set', 'A sleek black ballpoint pen with smooth ink flow');
INSERT INTO product_category VALUES ('004', 'Executive Portfolio', 'A sleek black ballpoint pen with smooth ink flow');
INSERT INTO product_category VALUES ('005', 'Assorted Gel Pen', 'A sleek black ballpoint pen with smooth ink flow');
INSERT INTO product_category VALUES ('006', 'Desktop Organizer', 'A sleek black ballpoint pen with smooth ink flow');
INSERT INTO product_category VALUES ('007', 'Pastel Highlighter', 'A sleek black ballpoint pen with smooth ink flow');
INSERT INTO product_category VALUES ('008', 'Whiteboard Eraser', 'A sleek black ballpoint pen with smooth ink flow');
INSERT INTO product_category VALUES ('009', 'Fountain Pen Set', 'A sleek black ballpoint pen with smooth ink flow');
INSERT INTO product_category VALUES ('010', 'Classic Black Pen', 'A sleek black ballpoint pen with smooth ink flow');
ALTER TABLE product_category MODIFY description VARCHAR(100);

UPDATE product_category SET description = 'A beautiful floral-patterned notebook with lined pages' WHERE pc_id = '002';
UPDATE product_category SET description = 'A set of colorful sticky notes in various shapes and sizes' WHERE pc_id = '003';
UPDATE product_category SET description = 'A portfolio with multiple compartments for documents, cards, and a pen loop.' WHERE pc_id = '004';
UPDATE product_category SET description = 'A gel pen in assorted colors, perfect for creative writing and drawing.' WHERE pc_id = '005';
UPDATE product_category SET description = 'A desktop organizer with space for pens, pencils, paper clips, and other office supplies.' WHERE pc_id = '006';
UPDATE product_category SET description = 'A set of pastel-colored highlighters for emphasizing important notes and passages.' WHERE pc_id = '007';
UPDATE product_category SET description = 'An eraser for whiteboards, featuring a felt bottom for smooth wiping' WHERE pc_id = '008';
UPDATE product_category SET description = 'A fountain pen set with a refillable ink cartridge and a stylish pen stand.' WHERE pc_id = '009';
UPDATE product_category SET description = 'A planner organizer with monthly and weekly calendars, to-do lists' WHERE pc_id = '010';
select * from product_category;

create table product_inventory(pi_id numeric(10),name varchar(20), quantity numeric(50), primary key(pi_id));
select * from product_inventory;
INSERT INTO product_inventory VALUES ('001', 'Classic Black Pen', 50);
INSERT INTO product_inventory VALUES ('002', 'Floral Notebook', 100);
INSERT INTO product_inventory VALUES ('003', 'Sticky Notes Set', 200);
INSERT INTO product_inventory VALUES ('004', 'Executive Portfolio', 30);
INSERT INTO product_inventory VALUES ('005', 'Assorted Gel Pen', 80);
INSERT INTO product_inventory VALUES ('006', 'Desktop Organizer', 150);
INSERT INTO product_inventory VALUES ('007', 'Pastel Highlighter', 70);
INSERT INTO product_inventory VALUES ('008', 'Whiteboard Eraser', 120); 
INSERT INTO product_inventory VALUES ('009', 'Fountain Pen Set', 40);
INSERT INTO product_inventory VALUES ('010', 'Planner Organizer', 90);


create table Discount(d_id numeric(10),name varchar(20), description varchar(50), price numeric(50), 
d_active char(1),primary key(d_id));
select * from Discount;
ALTER TABLE Discount MODIFY description VARCHAR(100);

INSERT INTO Discount VALUES ('001', 'Classic Black Pen', 'A sleek black ballpoint pen with smooth ink flow, perfect for everyday use.', 5.99, 'A');
INSERT INTO Discount VALUES ('002', 'Floral Notebook', 'A beautiful floral-patterned notebook with lined pages', 3.49, 'B');
INSERT INTO Discount VALUES ('003', 'Sticky Notes Set', 'A set of colorful sticky notes in various shapes and sizes', 1.99, 'C');
INSERT INTO Discount VALUES ('004', 'Executive Portfolio', 'A portfolio with multiple compartments for documents, cards, and a pen loop.', 7.99, 'D');
INSERT INTO Discount VALUES ('005', 'Assorted Gel Pen', 'A gel pen in assorted colors, perfect for creative writing and drawing.', 9.99, 'E');
INSERT INTO Discount VALUES ('006', 'Desktop Organizer', 'A desktop organizer with space for pens, pencils, paper clips, and other office supplies.', 12.49, 'F');
INSERT INTO Discount VALUES ('007', 'Pastel Highlighter', 'A set of pastel-colored highlighters for emphasizing important notes and passages.', 4.29, 'G');
INSERT INTO Discount VALUES ('008', 'Whiteboard Eraser', 'An eraser for whiteboards, featuring a felt bottom for smooth wiping', 2.79, 'H');
INSERT INTO Discount VALUES ('009', 'Fountain Pen Set', 'A fountain pen set with a refillable ink cartridge and a stylish pen stand.', 6.99, 'I');
INSERT INTO Discount VALUES ('010', 'Planner Organizer', 'A planner organizer with monthly and weekly calendars, to-do lists', 1.49, 'K');


create table product(p_id numeric(10),pc_id numeric(10),pi_id numeric(10),d_id numeric(10),name varchar(20), description varchar(100), price int(100),
foreign key(pc_id) references product_category(pc_id),foreign key(pi_id) references product_inventory(pi_id),
foreign key(d_id) references Discount(d_id), primary key(p_id));


select * from product;
INSERT INTO product VALUES ('001', '001', '001', '001', 'Classic Black Pen', 'A sleek black ballpoint pen with smooth ink flow, perfect for everyday use.', 5.99);
INSERT INTO product VALUES ('002', '002', '002', '002', 'Floral Notebook', 'A beautiful floral-patterned notebook with lined pages', 3.49);
INSERT INTO product VALUES ('003', '003', '003', '003', 'Sticky Notes Set', 'A set of colorful sticky notes in various shapes and sizes', 1.99);
INSERT INTO product VALUES ('004', '004', '004', '004', 'Executive Portfolio', 'A portfolio with multiple compartments for documents, cards, and a pen loop.', 7.99);
INSERT INTO product VALUES ('005', '005', '005', '005', 'Assorted Gel Pen', 'A gel pen in assorted colors, perfect for creative writing and drawing.', 9.99);
INSERT INTO product VALUES ('006', '006', '006', '006', 'Desktop Organizer', 'A desktop organizer with space for pens, pencils, paper clips, and other office supplies..', 12.49);
INSERT INTO product VALUES ('007', '007', '007', '007', 'Pastel Highlighter', 'A set of pastel-colored highlighters for emphasizing important notes and passages.', 4.29);
INSERT INTO product VALUES ('008', '008', '008', '008', 'Whiteboard Eraser', 'An eraser for whiteboards, featuring a felt bottom for smooth wiping', 2.79);
INSERT INTO product VALUES ('009', '009', '009', '009', 'Fountain Pen Set', 'A fountain pen set with a refillable ink cartridge and a stylish pen stand', 6.99);
INSERT INTO product VALUES ('010', '010', '010', '010', 'Planner Organizer', 'A planner organizer with monthly and weekly calendars, to-do lists', 1.49);


create table order_detail(od_id numeric(10), user_id numeric(10), total DECIMAL(10,2), payment_id numeric(65),
foreign key(user_id) references user(user_id), primary key(od_id));
ALTER TABLE order_detail MODIFY payment_id VARCHAR(50);
ALTER TABLE order_detail
DROP FOREIGN KEY order_detail_ibfk_1;

ALTER TABLE order_detail
DROP FOREIGN KEY user_id;

INSERT INTO order_detail VALUES ('001', 1001, 15.99, '123');
INSERT INTO order_detail VALUES ('002', 1002, 10.5, '124');
INSERT INTO order_detail VALUES ('003', 1003, 25.75, '125');
INSERT INTO order_detail VALUES ('004', 1004, 8.25, '126');
INSERT INTO order_detail VALUES ('005', 1005, 12, '127');
INSERT INTO order_detail VALUES ('006', 1006, 18.49, '128');
INSERT INTO order_detail VALUES ('007', 1007, 6.75, '129');
INSERT INTO order_detail VALUES ('008', 1008, 14.2, '130');
INSERT INTO order_detail VALUES ('009', 1009, 9.99, '131');
INSERT INTO order_detail VALUES ('010', 1010, 11.35, '132');
select * from order_detail;


create table order_item(oi_id numeric(10), od_id numeric(10), p_id numeric(10), quantity numeric(50),
foreign key(od_id) references order_detail(od_id),foreign key(p_id) references product(p_id),primary key(oi_id));
select * from order_item;
INSERT INTO order_item  VALUES
('001', '001', 1, 50),
('002', '002', 2, 100),
('003', '003', 3, 200),
('004', '004', 4, 30),
('005', '005', 5, 80),
('006', '006', 6, 150),
('007', '007', 7, 70),
('008', '008', 8, 120),
('009', '009', 9, 40),
('010', '010', 10, 90);


create table user(user_id numeric(10), username varchar(20),u_password varchar(20), f_name varchar(25),l_name varchar(25),
phone_no numeric(25),primary key(user_id));
select * from user;
INSERT INTO user VALUES
(1001, 'user1', 'pass123', 'John', 'Smith', '1234567890'),
(1002, 'user2', 'abc456', 'Emily', 'Johnson', '2345678901'),
(1003, 'user3', '789pass', 'Michael', 'Williams', '3456789012'),
(1004, 'user4', 'qwerty', 'Sarah', 'Brown', '4567890123'),
(1005, 'user5', '123abc', 'David', 'Jones', '5678901234'),
(1006, 'user6', 'pass456', 'Jennifer', 'Davis', '6789012345'),
(1007, 'user7', '456def', 'Christopher', 'Miller', '7890123456'),
(1008, 'user8', 'ilove123', 'Jessica', 'Wilson', '8901234567'),
(1009, 'user9', 'p@ssword', 'Andrew', 'Moore', '9012345678'),
(1010, 'user10', '123456', 'Samantha', 'Taylor', '0123456789');
select * from user;


create table shopping_session(ss_id numeric(10), user_id numeric(10), total int(50),
foreign key(user_id) references user(user_id),primary key(ss_id));
select * from shopping_session;
INSERT INTO shopping_session VALUES
('001', 1001, 15.99),
('002', 1002, 10.5),
('003', 1003, 25.75),
('004', 1004, 8.25),
('005', 1005, 12.00),
('006', 1006, 18.49),
('007', 1007, 6.75),
('008', 1008, 14.20),
('009', 1009, 9.99),
('010', 1010, 11.35);


create table cart_item(c_id numeric(10),ss_id numeric(10),p_id numeric(10),quantity numeric(50),
foreign key(p_id) references product(p_id),foreign key(ss_id) references shopping_session(ss_id),primary key(c_id));
select * from cart_item;
INSERT INTO cart_item VALUES
('123', '001', 1, 50),
('456', '002', 2, 100),
('789', '003', 3, 200),
('012', '004', 4, 30),
('345', '005', 5, 80),
('678', '006', 6, 150),
('901', '007', 7, 70),
('234', '008', 8, 120),
('567', '009', 9, 40),
('890', '010', 10, 90);



create table user_address(ua_id numeric(10), user_id numeric(10), address varchar(50),city varchar(25),
pincode numeric(25),state varchar(50),country varchar(50),phone_no numeric(25),foreign key(user_id) references user(user_id)
,primary key(ua_id));
select * from user_address;
INSERT INTO user_address VALUES
(105782, 1001, '123 Main Street', 'Anytown', 12345, 'California', 'USA', '1234567890'),
(205461, 1002, '456 Elm Street', 'Smallville', 54321, 'Kansas', 'USA', '2345678901'),
(307894, 1003, '789 Oak Street', 'Metro City', 67890, 'New York', 'USA', '3456789012'),
(409231, 1004, '987 Maple Street', 'Rivertown', 45678, 'Texas', 'USA', '4567890123'),
(512304, 1005, '321 Birch Street', 'Sunnydale', 98765, 'California', 'USA', '5678901234'),
(614527, 1006, '654 Pine Street', 'Lakeside', 23456, 'Washington', 'USA', '6789012345'),
(718945, 1007, '852 Cedar Street', 'Oceanview', 34567, 'Florida', 'USA', '7890123456'),
(821763, 1008, '369 Walnut Street', 'Hill Valley', 87654, 'California', 'USA', '8901234567'),
(929874, 1009, '753 Spruce Street', 'Riverdale', 56789, 'New York', 'USA', '9012345678'),
(1036589, 1010, '159 Ash Street', 'Pleasantville', 43210, 'Ohio', 'USA', '0123456789');



create table user_payment(up_id numeric(10), user_id numeric(10), payment_type varchar(10), account_no numeric(15),
expiry date not null,foreign key(user_id) references user(user_id),primary key(up_id));
select * from user_payment;
INSERT INTO user_payment VALUES
(123456789, 1001, 'Credit', '123456789012', '2026-05-01'), 
(987654321, 1002, 'Debit', '567812349012', '2025-09-01'), 
(456789012, 1003, 'PayPal', null , '2025-09-01'),
(321098765, 1004, 'Credit', '789012345678', '2027-03-01'), 
(789012345, 1005, 'Cash', null , '2025-09-01'),
(234567890, 1006, 'Debit', '345678901234', '2025-11-01'), 
(890123456, 1007, 'Credit', '901234567890', '2026-08-01'), 
(567890123, 1008, 'PayPal', null , '2025-09-01'),
(345678901, 1009, 'Credit', '678901234567', '2028-02-01'),
(901234567, 1010, 'Debit', '901234567890', '2025-06-01'); 


create table payment_details(payment_id numeric(10), oi_id numeric(10),od_id numeric(10),
 amount int(50), provider varchar(50), status varchar(50), c_id numeric(10),
foreign key(c_id) references cart_item(c_id),foreign key(od_id) references order_detail(od_id),
foreign key(oi_id) references order_item(oi_id), primary key(payment_id));
select * from payment_details;
INSERT INTO payment_details (payment_id, oi_id, od_id, amount, provider, status, c_id) VALUES
('123', '001', '001', 15.99, 'Office Depot', 'Shipped', '123'),
('124', '002', '002', 8.50, 'Staples', 'Processing', '456'),
('125', '003', '003', 12.25, 'Walmart', 'Delivered', '789'),
('126', '004', '004', 6.75, 'Amazon', 'Pending', '012'),
('127', '005', '005', 10.00, 'Target', 'Shipped', '345'),
('128', '006', '006', 9.99, 'Office Max', 'Processing', '678'),
('129', '007', '007', 5.50, 'Staples', 'Delivered', '901'),
('130', '008', '008', 7.25, 'Walmart', 'Pending', '234'),
('131', '009', '009', 14.50, 'Amazon', 'Shipped', '567'),
('132', '010', '010', 11.75, 'Target', 'Processing', '890');


create table shipping (ship_id numeric(10), payment_id numeric(10), user_id numeric(10), status varchar(50), Received char(1),
foreign key(payment_id) references payment_details(payment_id),foreign key(user_id) references user(user_id),
 primary key(ship_id));
 select * from shipping;
 INSERT INTO shipping (ship_id, payment_id, user_id, status, Received) VALUES
('001', '123', 1001, 'Shipped', 'Y'),
('002', '124', 1002, 'Processing', 'N'),
('003', '125', 1003, 'Delivered', 'Y'),
('004', '126', 1004, 'Pending', 'Y'),
('005', '127', 1005, 'Shipped', 'N'),
('006', '128', 1006, 'Processing', 'Y'),
('007', '129', 1007, 'Delivered', 'N'),
('008', '130', 1008, 'Pending', 'Y'),
('009', '131', 1009, 'Shipped', 'Y'),
('010', '132', 1010, 'Processing', 'N');



#20 SQL QUERIES 
#Query 1: Count the number of products in each category.
SELECT product_category.pc_id, product_category.name, COUNT(*) AS product_count
FROM product_category
JOIN product ON product_category.pc_id = product.pc_id
GROUP BY product_category.pc_id;



#Query 2: Calculate the total quantity of products in inventory
SELECT SUM(quantity) AS total_quantity
FROM product_inventory;


#Query 3: Find the average price of products.
SELECT AVG(price) AS average_price
FROM product;

#Query 4: Find the minimum and maximum price of products.
SELECT MIN(price) AS min_price, MAX(price) AS max_price
FROM product;

#Query 5: Find all products with a price greater than the average price.(Nested Query)
SELECT *
FROM product
WHERE price > (SELECT AVG(price) FROM product);

#Query 6: Find all users who have placed orders.
SELECT DISTINCT user_id
FROM order_detail;

#Query 7: Find all products that have been ordered.
SELECT DISTINCT p_id
FROM order_item;

#Query 8: List all products and their categories.
SELECT product.name, product_category.name AS category
FROM product
JOIN product_category ON product.pc_id = product_category.pc_id;

#Query 9: List all orders and their corresponding users.
SELECT order_detail.od_id, user.username
FROM order_detail
JOIN user ON order_detail.user_id = user.user_id;

#Query 10: List all products in an order, including product details.
SELECT order_item.oi_id, product.name, product.description
FROM order_item
JOIN product ON order_item.p_id = product.p_id;

#Query 11: Create a view to list all products with their categories.
CREATE VIEW product_category_view AS
SELECT product.name, product_category.name AS category
FROM product
JOIN product_category ON product.pc_id = product_category.pc_id;

#Query 12: Use the view to find all products in the "Classic Black Pen" category.
SELECT *
FROM product_category_view
WHERE category = 'Classic Black Pen';

#Query 13: List all users and their addresses, including users without addresses.
SELECT user.user_id, user.username, user_address.address
FROM user
LEFT JOIN user_address ON user.user_id = user_address.user_id
UNION
SELECT user.user_id, user.username, user_address.address
FROM user
RIGHT JOIN user_address ON user.user_id = user_address.user_id;


#14) Give the total od the price when the discount was given;
select sum(price) from Discount;




#15) Arrange all order item based on their quantities in ascending order.
select*from order_item order by quantity ASC;

#Query 16: List all products and their inventory details, including products without inventory.
SELECT product.name, product_inventory.quantity
FROM product
LEFT JOIN product_inventory ON product.pi_id = product_inventory.pi_id;

#Query 17: List all inventory items and their corresponding products, including inventory items without products.
SELECT product_inventory.name, product.p_id
FROM product_inventory
RIGHT JOIN product ON product_inventory.pi_id = product.pi_id;

#Query 18: List all users and their addresses, including users without addresses.
SELECT user.user_id, user.username, user_address.address
FROM user
LEFT JOIN user_address ON user.user_id = user_address.user_id
UNION
SELECT user.user_id, user.username, user_address.address
FROM user
RIGHT JOIN user_address ON user.user_id = user_address.user_id;

#Query 19: Find the total quantity of products ordered by each user, filtering for users who have ordered more than 100 products.
SELECT user_id, SUM(total) AS TotalSales
FROM order_detail
GROUP BY user_id;


#Query 20: List all orders and their corresponding users.
SELECT order_detail.od_id, user.username
FROM order_detail
INNER JOIN user ON order_detail.user_id = user.user_id;

