# UN Portal – Staff Management System

A Django-based web application for managing staff information, authentication, and administrative operations.
The system provides secure login/logout, staff listing, and staff creation features with a clean, professional interface.

---

## 🚀 Features

* User authentication (login & logout)
* Protected dashboard using Django authentication
* Add and view staff records
* Responsive and professional UI
* CSRF-protected forms
* Admin panel for system management

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS (Django Templates)
* **Database:** SQLite (default, can be replaced with PostgreSQL/MySQL)
* **Authentication:** Django built-in auth system

---

## 📁 Project Structure

```
un_portal/
├── dashboard/
│   ├── migrations/
│   ├── templates/
│   │   └── un_portal/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── add_staff.html
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── templates/
│   └── registration/
│       └── login.html
├── db.sqlite3
├── manage.py
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone <repository-url>
cd un_portal
```

### 2️⃣ Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
```

### 3️⃣ Install dependencies

```bash
pip install django
```

### 4️⃣ Run migrations

```bash
python manage.py migrate
```

### 5️⃣ Create superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the development server

```bash
python manage.py runserver
```

Access the app at:

```
http://127.0.0.1:8000/
```

---

## 🔐 Authentication

* Login URL: `/accounts/login/`
* Logout URL: `/accounts/logout/`
* Admin Panel: `/admin/`

Redirects are configured in `settings.py`:

```python
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
```

---

## 🧑‍💼 Staff Management

* View all staff on the home page
* Add new staff using the **Add Staff** button
* Access restricted to authenticated users

---

## 🛡️ Security

* CSRF protection enabled
* Login-required views
* Secure logout via POST requests

---

## 📌 Future Improvements

* Role-based access control
* Staff edit and delete functionality
* Search and pagination
* REST API / GraphQL integration
* Deployment using Docker or cloud services

---

## 📄 License

This project is for educational and internal use.
You may modify and extend it as needed.

---

## 👤 Author

Developed by **Sammy Magucha**

---


