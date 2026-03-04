# B+ Tree Based Student Database Management System

## 📌 Project Overview
This DBMS mini project is developed by **Sanchit Singh**, a B.Tech CSE 2nd year student at *Mahatma Jyotiba Phule Rohilkhand University*. It demonstrates B+ Tree indexing using MySQL and Python to manage student records and improve search performance.

## 🚀 Features
- Insert student records into the database  
- Search students by ID (Primary Key)  
- Search students by marks (Indexed search)  
- Display all records  
- Measure and compare execution time of indexed vs non-indexed queries

## 🛠️ Technologies Used
- Python 3  
- MySQL  
- mysql-connector-python  
- B+ Tree Indexing with InnoDB

## 🗄️ Database Structure
**Database:** `BplusTree`  
**Table:** `student`  
Fields:
- `id` (Primary Key)  
- `name`  
- `marks`  
- `department`  
- `created_at`

Indexes created:
- Primary key index on `id`  
- B+ Tree index on `marks`  
- Composite index on `(name, marks)`

## ▶️ How to Run
1. Install MySQL and start the server  
2. Run the SQL script `db.txt` to create database and table  
3. Install Python connector:


## 📊 Performance Analysis
This project compares:
- Primary key search time  
- Indexed search time using B+ Tree  
- Range queries without index  
Execution times are displayed to show the efficiency of indexed queries.

## 🎯 Learning Outcomes
- Understanding B+ Tree indexing and its role in DBMS  
- Practical exposure to creating and using indexes in MySQL  
- Evaluating query performance  
- Integrating Python with a SQL database

## 📁 Repository Contents
- `frontend.py` — Python CLI interface  
- `db.txt` — SQL script for database setup  
- `README.md` — Project documentation

---

⭐ Feel free to customize further with screenshots, schema diagrams, or usage examples!Install Python connector:
5. 
