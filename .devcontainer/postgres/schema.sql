CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price NUMERIC(10, 2),
    stock_quantity INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    order_date DATE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
a compra CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id),
    item_id INTEGER REFERENCES items(id),
    quantity INTEGER NOT NULL,
    unit_price NUMERIC(10, 2) NOT NULL
);
INSERT INTO items (name, category, price, stock_quantity)
VALUES ('Laptop', 'Electronics', 1200.00, 50),
    ('Smartphone', 'Electronics', 800.00, 150),
    ('Desk Chair', 'Furniture', 250.50, 75),
    ('Coffee Maker', 'Appliances', 89.99, 200),
    ('Running Shoes', 'Apparel', 120.00, 300),
    ('Gaming Mouse', 'Electronics', 75.50, 250),
    ('4K Monitor', 'Electronics', 450.00, 100),
    (
        'Mechanical Keyboard',
        'Electronics',
        150.00,
        120
    ),
    ('Bookshelf', 'Furniture', 180.75, 60);
INSERT INTO customers (first_name, last_name, email)
VALUES ('Ana', 'Silva', 'ana.silva@email.com'),
    ('Bruno', 'Costa', 'bruno.costa@email.com'),
    ('Carla', 'Mendes', 'carla.mendes@email.com'),
    ('Daniel', 'Pereira', 'daniel.pereira@email.com'),
    ('Eduarda', 'Lima', 'eduarda.lima@email.com');
INSERT INTO orders (customer_id, order_date)
VALUES (1, '2023-10-01');
INSERT INTO order_items (order_id, item_id, quantity, unit_price)
VALUES (1, 1, 1, 1200.00),
    (1, 7, 2, 450.00);
INSERT INTO orders (customer_id, order_date)
VALUES (2, '2023-10-05');
INSERT INTO order_items (order_id, item_id, quantity, unit_price)
VALUES (2, 2, 1, 800.00),
    (2, 3, 1, 250.50);
INSERT INTO orders (customer_id, order_date)
VALUES (3, '2023-10-12');
INSERT INTO order_items (order_id, item_id, quantity, unit_price)
VALUES (3, 1, 2, 1200.00),
    (3, 6, 1, 75.50),
    (3, 8, 1, 150.00);
INSERT INTO orders (customer_id, order_date)
VALUES (4, '2023-10-15');
INSERT INTO order_items (order_id, item_id, quantity, unit_price)
VALUES (4, 2, 1, 800.00);
INSERT INTO orders (customer_id, order_date)
VALUES (1, '2023-10-20');
INSERT INTO order_items (order_id, item_id, quantity, unit_price)
VALUES (5, 6, 2, 75.50);
INSERT INTO orders (customer_id, order_date)
VALUES (5, '2023-10-22');
INSERT INTO order_items (order_id, item_id, quantity, unit_price)
VALUES (6, 4, 1, 89.99);
