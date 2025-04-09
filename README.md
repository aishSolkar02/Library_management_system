# 📘 Library Management System

A simple and user-friendly Library Management System built using **Django 4.2** and **MySQL**.  
This project includes authentication and full CRUD operations for managing books.

---

## 🔹 Key Features

- User Registration & Login
- Add, View, Edit, and Delete Books
- Clean and Responsive UI
- Django Admin Panel Integration
- MySQL Database Support

---

## 🔧 Technologies Used

- **Python**
- **Django 4.2**
- **MySQL**
- **HTML, CSS**
- **Git & GitHub**

---

## 🚀 How to Run

```bash
git clone https://github.com/aishSolkar02/Library_management_system.git
cd Library_management_system

# Create & activate virtual environment
python -m venv env
env\Scripts\activate  # for Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the server
python manage.py runserver


 Testing
Unit tests are written using Django's built-in TestCase class.

Tests cover:

✅ Book model creation
✅ Book views: list, create, update, delete
✅ User login required for actions

**To run the tests:**
python manage.py test
