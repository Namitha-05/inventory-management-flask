import sqlite3

# Connect to SQLite (creates database if it doesn't exist)
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Drop old tables (avoid conflicts)
cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS locations")

# Create Products table
cursor.execute("""
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity INTEGER DEFAULT 0
)
""")

# Create Locations table
cursor.execute("""
CREATE TABLE locations (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

# Insert sample products
cursor.executemany("INSERT INTO products (name, quantity) VALUES (?, ?)", [
    ("Product A", 100),
    ("Product B", 50),
    ("Product C", 75)
])

# Insert sample locations
cursor.executemany("INSERT INTO locations (name) VALUES (?)", [
    ("Warehouse X",),
    ("Warehouse Y",),
    ("Shop Front",)
])

conn.commit()
conn.close()

print(" Database created and seeded successfully!")
