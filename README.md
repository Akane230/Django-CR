# Text Records Django Web Application

## Project Overview

This project is a simple web application built using **Django** and a relational database.
It demonstrates basic database **write and read operations** triggered directly through HTTP URL access.

The application allows:

* Inserting text records into a database
* Retrieving and displaying all stored records via the browser

---

## Technologies Used

* Python
* Django Framework
* SQLite (default Django relational database)

---

## Features

* Properly configured Django project with database integration
* A database table for storing text-based records
* URL endpoint for inserting data into the database
* URL endpoint for retrieving and displaying stored data
* Successful database migrations and ORM usage

---

## Project Setup Instructions

### 1. Clone or Download the Project

```bash
git clone <repository-url>
cd textproject
```

### 2. Install Dependencies

```bash
pip install django
```

### 3. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Start the Development Server

```bash
python manage.py runserver
```

---

## URL Endpoints

### `/add`

* Inserts a new text record into the database.
* Access via browser:

```
http://127.0.0.1:8000/add
```

### `/show`

* Retrieves and displays all stored text records.
* Access via browser:

```
http://127.0.0.1:8000/show
```

---

## Database Structure

### TextRecord Table

| Field Name | Type |
| ---------- | ---- |
| content    | Text |

---

## Validation

* Visiting `/add` successfully stores a record in the database.
* Visiting `/show` displays all previously stored records.
* Repeated access to `/add` results in multiple records being saved and shown.

---

## Conclusion

This project validates basic CRUD operations using Django’s ORM and demonstrates database persistence and retrieval through HTTP URL access.
