import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Hardcoded secret (Sensitive Information Exposure)
SECRET_KEY = "hardcoded_secret_key"

# Connect to a SQLite database (database.db)
def get_db_connection():
    connection = sqlite3.connect("database.db")
    return connection

# Vulnerable to SQL Injection
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Directly embedding user input in SQL query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("Executing query:", query)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)  # No parameterized query
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return "Login successful!"
    else:
        return "Invalid credentials!"

# Improper error handling
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        file = request.files['file']
        file.save(f"uploads/{file.filename}")  # Directory traversal possible
        return "File uploaded successfully!"
    except Exception as e:
        return f"An error occurred: {e}"  # Exposes internal error details

# No rate-limiting or input validation
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE content LIKE '%{query}%'")  # Vulnerable to SQL Injection
    results = cursor.fetchall()
    conn.close()
    return {"results": results}

if __name__ == "__main__":
    app.run(debug=True)
