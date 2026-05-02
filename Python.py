from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "tiger",
    "database": "btree_db"
}

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM Users WHERE username=%s AND password=%s", (data['username'], data['password']))
    res = cursor.fetchone()
    conn.close()
    if res: return jsonify({"status": "success", "role": res[0]})
    return jsonify({"status": "error", "message": "Access Denied"}), 401

@app.route("/add", methods=["POST"])
def add():
    if request.headers.get("X-User-Role") != "admin": return jsonify({"error": "Forbidden"}), 403
    data = request.json
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Student(name,course,marks) VALUES(%s,%s,%s)", (data['name'], data['course'], data['marks']))
    conn.commit()
    conn.close()
    return jsonify({"status": "added"})

@app.route("/view")
def view():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Student ORDER BY student_id")
    res = cursor.fetchall()
    conn.close()
    return jsonify(res)

@app.route("/search/<int:id>")
def search(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Student WHERE student_id=%s", (id,))
    res = cursor.fetchone()
    conn.close()
    return jsonify(res)

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    if request.headers.get("X-User-Role") != "admin": return jsonify({"error": "Forbidden"}), 403
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Student WHERE student_id=%s", (id,))
    conn.commit()
    conn.close()
    return jsonify({"status": "deleted"})

if __name__ == "__main__":
    print("\n" + "═"*60)
    print(f" NEXUS B+ TREE DBMS - CORE ENGINE ONLINE")
    print(f" DEVELOPED BY: Sanchit Singh (24CS91)")
    print(f" WEBSITE CREATED: a2careindia.com")
    print(f" SOCIAL MEDIA: ")
    print(f"   - LinkedIn:  https://www.linkedin.com/in/sanchit3/")
    print(f"   - Instagram: https://www.instagram.com/sanchit_s01/")
    print(f"   - YouTube:   https://www.youtube.com/channel/UCEQmewlFct_uFf5IL6aIH-A?sub_confirmation=1")
    print("═"*60 + "\n")
    app.run(debug=True, port=5000)
