from flask import Flask, jsonify, request
import sqlite3
from passlib.hash import bcrypt
import uuid

app = Flask(__name__)

def get_db_connection():
    """Returns a connection to the SQLite database."""
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def hash_password(password):
    """Hash the password using passlib's bcrypt."""
    return bcrypt.hash(password)

def verify_password(password, hashed_password):
    """Verify the password against the hashed password."""
    return bcrypt.verify(password, hashed_password)


# =============== Simple APIs ===============

@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"message": "Welcome to the API!"})

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    if num1 is None or num2 is None:
        return jsonify({"error": "Please provide two numbers"}), 400
    return jsonify({"result": num1 + num2})


# =============== Intermediate APIs ===============

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username is None:
        return jsonify({"error": "Please provide username"}), 400

    elif password is None:
        return jsonify({"error": "Please provide password"}), 400

    
    with get_db_connection() as conn:
        cursor = conn.cursor()
        users = cursor.execute("SELECT * FROM users").fetchall()

        if any(user["username"] == username for user in users):
            return jsonify({"error": "Username already exist"}), 409

        hashed_password = hash_password(password)
        try:
            cursor.execute(
                "INSERT INTO users (id, username, password) VALUES (?, ?, ?)", 
                (str(uuid.uuid4()), username, hashed_password)
            )
            conn.commit()
        except sqlite3.Error as e:
            return jsonify({"error": str(e)}), 500
        
        return jsonify({"message": "User added successfully"}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get('password')

    if username is None:
        return jsonify({"error": "Please provide username"}), 400
    elif password is None:
        return jsonify({"error": "Please provide password"}), 400
    
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            users = cursor.execute("SELECT * FROM users").fetchall()

            user = next((user for user in users if user["username"] == username), None)

            if not user:
                return jsonify({"error": "User not found"}), 404

            if verify_password(password, user["password"]):
                return jsonify({"message": "Login success"}), 200
            return jsonify({"error": "Invalid credentials"}), 401

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@app.route('/users', methods=['GET'])
def get_users():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, username FROM users")
        users = cursor.fetchall()

        return jsonify({ "data" : [dict(user) for user in users] }), 200


if __name__ == '__main__':
    app.run(debug=True)
