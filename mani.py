
# Online Python - IDE, Editor, Compiler, Interpreter
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database setup for mock data
def create_db():
    conn = sqlite3.connect('mock_db.sqlite')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Customers (Name TEXT, Age INTEGER, City TEXT)''')
    cursor.execute("INSERT OR IGNORE INTO Customers VALUES ('Alice', 30, 'London'), ('Bob', 40, 'New York')")
    conn.commit()
    conn.close()

@app.route('/validate_query', methods=['POST'])
def validate_query():
    user_query = request.json.get('query')
    try:
        conn = sqlite3.connect('mock_db.sqlite')
        cursor = conn.cursor()
        cursor.execute(user_query)
        result = cursor.fetchall()
        return jsonify({"status": "success", "data": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
    finally:
        conn.close()

if __name__ == '__main__':
    create_db()
    app.run(debug=True)


