🌳 B+ Tree Based Student Database Management System (Web Version)
📌 Project Overview

This project is developed by Sanchit Singh (B.Tech CSE, 2nd Year, Mahatma Jyotiba Phule Rohilkhand University).

It is a full-stack DBMS application that demonstrates a manual implementation of B+ Tree indexing using MySQL, integrated with a Flask backend and an interactive web frontend.

💡 Focus: Efficient data retrieval using B+ Tree traversal instead of traditional search.

🚀 Features

✨ Insert student records through UI
🔍 Search using B+ Tree Index Traversal
📄 View all records dynamically
❌ Delete records instantly
🌳 Custom B+ Tree (Order = 4)
🔗 REST API with Flask
🎨 Clean web interface (HTML + CSS + JS)

🛠️ Tech Stack
Layer	Technology
Frontend	HTML, CSS, JavaScript
Backend	Python (Flask)
Database	MySQL
Connector	mysql-connector-python
Concept	B+ Tree Indexing
🗄️ Database Design

Database: btree_db

📊 Tables Overview
Student → Stores main student data
Record → Maps keys for indexing
IndexTable → Stores index metadata
BPlusTreeIndex → Root + tree structure
Node → Represents tree nodes
Pointer → Connects nodes & records
🌳 B+ Tree Logic (Core Idea)
Order m = 4
Leaf nodes store actual record references
Automatic node splitting on overflow
Linked leaf nodes (next_node_id)
Fast lookup via index traversal
▶️ Setup & Execution
1️⃣ Install Dependencies
pip install flask flask-cors mysql-connector-python
2️⃣ Setup Database
Create database:
CREATE DATABASE btree_db;
Run your SQL schema file
3️⃣ Configure Backend

Update credentials in Python:

user = "root"
password = "your_password"
4️⃣ Run Flask Server
python app.py

🔗 Server URL: http://localhost:5000

5️⃣ Run Frontend
Open index.html in browser
OR
Use Live Server (VS Code)
🔌 API Endpoints
Method	Endpoint	Description
POST	/add	Insert student
GET	/search/<id>	Search via B+ Tree
GET	/view	View all records
DELETE	/delete/<id>	Delete record
📊 Performance Insight

✔ Faster search using B+ Tree traversal
✔ Efficient indexing vs linear scan
✔ Optimized data access structure

🎯 Learning Outcomes
📘 B+ Tree data structure (practical)
🗄️ Indexing in DBMS
🔗 Backend–Database integration
🌐 Full-stack project development
⚙️ Working with REST APIs
📁 Project Structure
📦 BPlusTree-DBMS
 ┣ 📜 index.html
 ┣ 📜 app.py
 ┣ 📜 database.sql
 ┗ 📜 README.md
📚 Important References
Database System Concepts — Silberschatz, Korth, Sudarshan
Database Management Systems — Raghu Ramakrishnan
Fundamentals of Database Systems — Elmasri & Navathe
The Art of Computer Programming (Vol. 3) — Donald Knuth
MySQL Official Documentation
Flask Official Documentation
GeeksforGeeks — B+ Tree & DBMS
TutorialsPoint — Indexing Concepts
🌟 Future Scope

🚀 Add update/edit feature
🌳 Visualize B+ Tree structure
🔐 Add authentication system
⚡ Improve tree balancing logic

⭐ Final Note

This project bridges theory (B+ Trees) with real-world implementation, making it ideal for DBMS learning and academic demonstrations.
