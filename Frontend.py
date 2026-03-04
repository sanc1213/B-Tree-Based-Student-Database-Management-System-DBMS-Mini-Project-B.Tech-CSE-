import mysql.connector
import time
import base64
import hashlib
import sys
# ==============================
# DATABASE CONNECTION
# ==============================
def create_connection():
    try:
        p = input("Enter DATABASE Password: ")
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=p,                     #NOTE: DATABASE PASSWORD should be Same as MySQL Database
            database="BplusTree"
        )
        print("✅ Connected Successfully")
        return conn
    except mysql.connector.Error as err:
        print("❌ Connection Failed:", err)
        return None


# ==============================
# TABULAR DISPLAY FUNCTION
# ==============================
def print_table(cursor, records):
    if not records:
        print("No records found.")
        return

    columns = [col[0] for col in cursor.description]

    col_width = []
    for i in range(len(columns)):
        max_len = len(columns[i])
        for row in records:
            max_len = max(max_len, len(str(row[i])))
        col_width.append(max_len + 2)

    for i in range(len(columns)):
        print(columns[i].ljust(col_width[i]), end="")
    print()

    for width in col_width:
        print("-" * width, end="")
    print()

    for row in records:
        for i in range(len(row)):
            print(str(row[i]).ljust(col_width[i]), end="")
        print()


# ==============================
# MENU
# ==============================
def menu():
    print("\n===== WELCOME TO B+ TREE DBMS PROJECT =====")
    print("🔒", __decrypt_creator())
    print("1. Insert Student")
    print("2. Search by ID (Primary Key)")
    print("3. Search by Marks (B+ Tree Index)")
    print("4. Show All Records")
    print("5. Performance Test")
    print("6. Exit")


# ==============================
# INSERT
# ==============================
def insert_student(cursor, conn):
    try:
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))
        dept = input("Enter Department: ")

        sql = "INSERT INTO student (id, name, marks, department) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, (id, name, marks, dept))
        conn.commit()
        print("✅ Student Inserted")

    except mysql.connector.Error as err:
        print("❌ Error:", err)
    except ValueError:
        print("❌ ID and Marks must be numbers!")

# ==============================
# 🔐 PROTECTED CREATOR SECTION
# ==============================

# Original Protected Text
__original_text = "Project is Created by SANCHIT SINGH BTECH CSE 2nd year"

# Encrypted Version (Auto-generated)
__encrypted_creator = base64.b64encode(__original_text.encode()).decode()

def __decrypt_creator():
    decoded = base64.b64decode(__encrypted_creator.encode()).decode()

    # Integrity Check
    original_hash = hashlib.sha256(__original_text.encode()).hexdigest()
    current_hash = hashlib.sha256(decoded.encode()).hexdigest()

    if current_hash != original_hash:
        print("❌ Unauthorized Modification Detected!")
        sys.exit()

    return decoded



# ==============================
# SEARCH BY ID
# ==============================
def search_by_id(cursor):
    try:
        id = int(input("Enter ID: "))
        start = time.time()

        cursor.execute("SELECT id, name, marks, department FROM student WHERE id=%s", (id,))
        result = cursor.fetchall()

        end = time.time()
        print_table(cursor, result)
        print("Time Taken:", round(end - start, 6), "seconds")

    except ValueError:
        print("❌ Invalid ID!")


# ==============================
# SEARCH BY MARKS
# ==============================
def search_by_marks(cursor):
    try:
        marks = int(input("Enter Marks: "))
        start = time.time()

        cursor.execute("SELECT id, name, marks, department FROM student WHERE marks=%s", (marks,))
        result = cursor.fetchall()

        end = time.time()
        print_table(cursor, result)
        print("Time Taken (B+ Tree Index):", round(end - start, 6), "seconds")

    except ValueError:
        print("❌ Invalid Marks!")


# ==============================
# SHOW ALL RECORDS
# ==============================
def show_all(cursor):
    cursor.execute("SELECT id, name, marks, department FROM student")
    records = cursor.fetchall()
    print_table(cursor, records)


# ==============================
# PERFORMANCE TEST
# ==============================
def performance_test(cursor):
    print("\nRunning Performance Test...")

    start = time.time()
    cursor.execute("SELECT id, name, marks, department FROM student WHERE marks > 50")
    cursor.fetchall()
    end = time.time()
    print("Range Query Time:", round(end - start, 6), "seconds")

    start = time.time()
    cursor.execute("SELECT id, name, marks, department FROM student WHERE marks = 85")
    cursor.fetchall()
    end = time.time()
    print("Indexed Search Time:", round(end - start, 6), "seconds")


# ==============================
# MAIN PROGRAM
# ==============================
def main():
    conn = create_connection()
    if conn is None:
        return

    cursor = conn.cursor()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == '1':
            insert_student(cursor, conn)
        elif choice == '2':
            search_by_id(cursor)
        elif choice == '3':
            search_by_marks(cursor)
        elif choice == '4':
            show_all(cursor)
        elif choice == '5':
            performance_test(cursor)
        elif choice == '6':
            print("Exiting Program...")
            break
        else:
            print("Invalid choice!")

    cursor.close()
    conn.close()
    print("✅ Connection Closed.")


# ==============================
# START PROGRAM
# ==============================
if __name__ == "__main__":
    main()
