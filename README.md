# 🏦 Bank Management System

A simple **Bank Account Management System** built using **Python (Tkinter + SQLite)**.  
This project provides both an **Admin Panel** and a **User Panel** for managing users and bank accounts.

---

## ✨ Features

### 👨‍💻 Admin
- Login with admin credentials (`admin / Admin123`)
- Create new users
- Delete users
- Disable users
- View all users in a Treeview table

### 👤 User
- Login with username & password
- Search accounts by **National Code** or **Account Number**
- Create new bank accounts
- Update account information
- Deposit money
- Withdraw money
- Disable accounts
- View all accounts in a Treeview table

---

## 🛠️ Tech Stack
- **Python 3**
- **Tkinter** (for GUI)
- **SQLite** (as the database)

---

## 📂 Project Structure
Bank-Management-System/
│── main.py # Main entry point (login + forms)
│── DataAccess/
│ └── user_data_access.py # Database operations (CRUD)
│── Entities/
│ ├── account.py # Account entity class
│ └── user.py # User entity class
│── BankManagement.db # SQLite database