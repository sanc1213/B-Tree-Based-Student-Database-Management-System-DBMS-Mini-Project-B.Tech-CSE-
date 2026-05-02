🌳 B+ Tree Based Student Database Management System (Web Version)
📌 Project Overview

This DBMS mini project is developed by Sanchit Singh, a B.Tech CSE 2nd year student at Mahatma Jyotiba Phule Rohilkhand University.

This version is a full-stack web application that demonstrates B+ Tree indexing implemented manually in MySQL and integrated with a Flask backend and HTML frontend for interactive student record management.

🚀 Features
➕ Insert student records via web interface
🔍 Search student by ID using B+ Tree Index traversal
📄 View all student records dynamically
❌ Delete records with real-time update
🌳 Custom implementation of B+ Tree (order = 4)
🔗 Backend API using Flask
🎨 Interactive frontend using HTML, CSS, JavaScript
🛠️ Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Python (Flask)
Database: MySQL
Connector: mysql-connector-python
Concept: B+ Tree Indexing (Manual Implementation)
🗄️ Database Structure

Database Name: btree_db

Tables:
Student
student_id (Primary Key)
name
course
marks
Record
Stores key values for indexing
Linked with Student using Foreign Key
IndexTable
Stores index metadata
BPlusTreeIndex
Maintains root node and tree structure
Node
Represents B+ Tree nodes (leaf/internal)
Pointer
Connects nodes and records
🌳 B+ Tree Implementation Details
Order of tree (m = 4)
Leaf nodes store record pointers
Automatic node splitting when overflow occurs
Linked leaf nodes using next_node_id
Index traversal used for fast searching
▶️ How to Run
1. Install Requirements
pip install flask flask-cors mysql-connector-python
2. Setup MySQL Database
Create database btree_db
Run the provided SQL script to create all tables
3. Configure Database

Update credentials in Python file:

user="root",
password="your_password"
4. Run Backend Server
python app.py

Server runs at:
http://localhost:5000

5. Run Frontend
Open the HTML file in browser
Or use Live Server (VS Code recommended)
🔌 API Endpoints
POST /add → Insert student
GET /search/<id> → Search using B+ Tree index
GET /view → View all records
DELETE /delete/<id> → Delete record
📊 Performance Insight

This project demonstrates:

Efficient searching using B+ Tree traversal
Reduced lookup time compared to linear search
Structured indexing using relational tables
🎯 Learning Outcomes
Deep understanding of B+ Tree data structure
Hands-on experience with indexing in DBMS
Building a full-stack database application
Implementing tree structures inside relational databases
API development using Flask
📁 Repository Contents
index.html — Frontend UI
app.py — Flask backend
database.sql — MySQL schema
README.md — Documentation
📚 Important References
Abraham Silberschatz, Henry F. Korth, S. Sudarshan — Database System Concepts
Raghu Ramakrishnan, Johannes Gehrke — Database Management Systems
Elmasri & Navathe — Fundamentals of Database Systems
Donald Knuth — The Art of Computer Programming (Vol. 3: Sorting and Searching)
MySQL Official Documentation — https://dev.mysql.com/doc/
Flask Official Documentation — https://flask.palletsprojects.com/
GeeksforGeeks — B+ Tree Data Structure Articles
TutorialsPoint — DBMS and Indexing Concepts
🌟 Future Improvements
Add update/edit functionality
Visualize B+ Tree structure graphically
Add authentication system
Optimize tree balancing logic