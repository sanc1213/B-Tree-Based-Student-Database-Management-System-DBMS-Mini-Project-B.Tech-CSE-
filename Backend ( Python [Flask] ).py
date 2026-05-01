from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# ===================================================
# DATABASE CONNECTION
# ===================================================
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger",  # Change password as needed
    database="btree_db"
)
cursor = db.cursor()

ORDER_M = 4 

def reset_student_id():
    cursor.execute("SELECT COUNT(*) FROM Student")
    if cursor.fetchone()[0] == 0:
        cursor.execute("ALTER TABLE Student AUTO_INCREMENT = 1")
        db.commit()

# ===================================================
# B+ TREE LOGIC (Corrected for Foreign Keys)
# ===================================================
def get_bplustree_index():
    cursor.execute("SELECT index_id, root_node_id FROM BPlusTreeIndex LIMIT 1")
    res = cursor.fetchone()
    if res: return res

    # 1. Create entry in IndexTable
    cursor.execute("INSERT INTO IndexTable(index_type) VALUES(%s)", ("B+ Tree",))
    index_id = cursor.lastrowid
    
    # 2. Create entry in BPlusTreeIndex (Placeholder root)
    cursor.execute("""
        INSERT INTO BPlusTreeIndex(index_id, root_node_id, order_m, height) 
        VALUES(%s, NULL, %s, 1)
    """, (index_id, ORDER_M))
    
    # 3. Create the Root Node (Links to BPlusTreeIndex)
    cursor.execute("""
        INSERT INTO Node(index_id, parent_node_id, node_type, num_keys, next_node_id) 
        VALUES(%s, NULL, 'leaf', 0, NULL)
    """, (index_id,))
    root_id = cursor.lastrowid
    
    # 4. Update BPlusTreeIndex with the actual root_node_id
    cursor.execute("UPDATE BPlusTreeIndex SET root_node_id = %s WHERE index_id = %s", (root_id, index_id))
    db.commit()
    return (index_id, root_id)

def insert_into_leaf(leaf_id, record_id):
    cursor.execute("SELECT num_keys FROM Node WHERE node_id=%s", (leaf_id,))
    num_keys = cursor.fetchone()[0]

    if num_keys < ORDER_M:
        cursor.execute("INSERT INTO Pointer(from_node_id, record_id) VALUES(%s,%s)", (leaf_id, record_id))
        cursor.execute("UPDATE Node SET num_keys=num_keys+1 WHERE node_id=%s", (leaf_id,))
        db.commit()
    else:
        split_leaf(leaf_id, record_id)

def split_leaf(leaf_id, new_record_id):
    cursor.execute("""
        SELECT P.record_id, R.key_value FROM Pointer P 
        JOIN Record R ON P.record_id = R.record_id 
        WHERE P.from_node_id=%s
    """, (leaf_id,))
    data = cursor.fetchall()
    
    cursor.execute("SELECT key_value FROM Record WHERE record_id=%s", (new_record_id,))
    new_val = cursor.fetchone()[0]
    data.append((new_record_id, new_val))
    data.sort(key=lambda x: x[1]) 

    mid = len(data) // 2
    left_data, right_data = data[:mid], data[mid:]

    cursor.execute("SELECT next_node_id, index_id FROM Node WHERE node_id=%s", (leaf_id,))
    row = cursor.fetchone()
    old_next_id, idx_id = row[0], row[1]

    # Update Left Node
    cursor.execute("DELETE FROM Pointer WHERE from_node_id=%s", (leaf_id,))
    for rid, val in left_data:
        cursor.execute("INSERT INTO Pointer(from_node_id, record_id) VALUES(%s,%s)", (leaf_id, rid))

    # Create Right Node
    cursor.execute("""
        INSERT INTO Node(index_id, parent_node_id, node_type, num_keys, next_node_id)
        VALUES (%s, NULL, 'leaf', %s, %s)
    """, (idx_id, len(right_data), old_next_id))
    right_id = cursor.lastrowid

    # Update Left to point to Right
    cursor.execute("UPDATE Node SET num_keys=%s, next_node_id=%s WHERE node_id=%s", 
                   (len(left_data), right_id, leaf_id))
    
    # Add Pointers to Right Node
    for rid, val in right_data:
        cursor.execute("INSERT INTO Pointer(from_node_id, record_id) VALUES(%s,%s)", (right_id, rid))
    db.commit()

# ===================================================
# ROUTES
# ===================================================

@app.route("/add", methods=["POST"])
def add_student():
    reset_student_id()
    data = request.json
    cursor.execute("INSERT INTO Student(name,course,marks) VALUES(%s,%s,%s)", 
                   (data['name'], data['course'], int(data['marks'])))
    student_id = cursor.lastrowid
    
    idx_id, root_id = get_bplustree_index()
    cursor.execute("INSERT INTO Record(student_id, key_value) VALUES(%s,%s)", (student_id, student_id))
    record_id = cursor.lastrowid
    
    insert_into_leaf(root_id, record_id)
    db.commit()
    return jsonify({"status": "added", "id": student_id})

@app.route("/search/<int:id>")
def search(id):
    cursor.execute("""
        SELECT S.student_id, S.name, S.course, S.marks FROM Student S
        JOIN Record R ON S.student_id = R.student_id
        JOIN Pointer P ON R.record_id = P.record_id
        WHERE R.key_value = %s
    """, (id,))
    res = cursor.fetchone()
    return jsonify(res) if res else jsonify(None)

@app.route("/view")
def view():
    cursor.execute("SELECT * FROM Student ORDER BY student_id")
    return jsonify(cursor.fetchall())

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    cursor.execute("DELETE FROM Student WHERE student_id=%s", (id,))
    db.commit()
    return jsonify({"status": "deleted"})

if __name__ == "__main__":
    app.run(debug=True)
