import sqlite3

connection = sqlite3.connect('/data/checkoutapp.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE Categories (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL
);
""")

connection.execute("""
CREATE TABLE Products (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    image_id VARCHAR NOT NULL,
    name VARCHAR NOT NULL, 
    price DOUBLE NOT NULL,
    category_id INTEGER,
    FOREIGN KEY(category_id) REFERENCES Categories(id)
);
""")

connection.execute("""
CREATE TABLE Orders (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    email VARCHAR NULL
);
""")

connection.execute("""
CREATE TABLE OrderPayment (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    payment_type CHAR NOT NULL,
    name_on_card VARCHAR NOT NULL,
    card_number VARCHAR NOT NULL,
    expiration VARCHAR NOT NULL,
    cvv VARCHAR NOT NULL,
    FOREIGN KEY(order_id) REFERENCES Orders(id)
);
""")

connection.execute("""
CREATE TABLE OrderItems (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(id),
    FOREIGN KEY (product_id) REFERENCES Products(id)
);
""")

connection.execute("""
INSERT INTO Categories(id, name) VALUES
    (1, 'Bakery'),
    (2, 'Entrees'),
    (3, 'Drinks');
""")

connection.execute("""
INSERT INTO Products(id, image_id, name, price, category_id) VALUES
    (1, '293202f9d9f7f4', 'Bagel b', 2.0, 1),
    (2, '808916fd5ddf96', 'Croissant', 1.0, 1),
    (3, '95d02a230fe050', 'Muffin', 1.25, 1),
    (4, '23f95765b967ff', 'Toast / Bread', 1, 1),
    (5, '5650be5d48a99b', 'English Muffin', 2.5, 1),
    (6, 'bd237a0c0d19ef', 'Pasta Bar', 12.99, 2),
    (7, '3e1bd1342800f7', 'Mediterranean Entree', 10.99, 2),
    (8, '72589c4c990f97', 'Indian Entree', 11.95, 2),
    (9, '70c2a6247e7b58', 'Small Drink', 0.75, 3),
    (10, 'dba0fc03da30ca', 'Medium Drink', 1.5, 3),
    (11, 'ffc9bf61e441cd', 'Large Drink', 2, 3),
    (12, 'ffc9bf61e441cd', 'Some desert 1', 2, 4),
    (13, 'ffc9bf61e441cd', 'Some desert 2', 2.5, 4),
    (14, 'ffc9bf61e441cd', 'Some desert 3', 4, 4);
""")


print("Schema created and seeded successfully")
connection.close()

