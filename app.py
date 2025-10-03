from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
DB_NAME = "inventory.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Access columns by name
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch products and locations
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    cursor.execute("SELECT * FROM locations")
    locations = cursor.fetchall()

    conn.close()

    return render_template("index.html", products=products, locations=locations)

if __name__ == "__main__":
    app.run(debug=True)
