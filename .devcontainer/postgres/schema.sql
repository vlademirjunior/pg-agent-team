CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price NUMERIC(10, 2),
    stock_quantity INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO items (name, category, price, stock_quantity) VALUES
('Laptop', 'Electronics', 1200.00, 50),
('Smartphone', 'Electronics', 800.00, 150),
('Desk Chair', 'Furniture', 250.50, 75),
('Coffee Maker', 'Appliances', 89.99, 200),
('Running Shoes', 'Apparel', 120.00, 300);
