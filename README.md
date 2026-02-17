---

# ✅ What You Are Building (Simple Overview)

A Django web app that:

* Has a database table storing **text records**
* `/add` → inserts a text record into the database
* `/show` → displays all stored records in the browser
* Uses **URL-triggered HTTP requests only** (no forms required)

---

# 1️⃣ Create the Django Project

```bash
django-admin startproject textproject
cd textproject
python manage.py startapp textapp
```

Your structure should look like:

```
textproject/
├── textproject/
│   ├── settings.py
│   ├── urls.py
├── textapp/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
└── manage.py
```

---

# 2️⃣ Configure the Database (Requirement ✔)

Open `settings.py`

### Register the app

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'textapp',
]
```

### Database configuration (default SQLite)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

✔ This already satisfies **“properly connected database backend”**

---

# 3️⃣ Create the Model (Database Table)

Open `textapp/models.py`

```python
from django.db import models

class TextRecord(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content
```

✔ This defines a **text-based database table**

---

# 4️⃣ Run Migrations (Requirement ✔)

```bash
python manage.py makemigrations
python manage.py migrate
```

✔ Table is now **created in the database**

---

# 5️⃣ Implement the `/add` View (Insert Record)

Open `textapp/views.py`

```python
from django.http import HttpResponse
from .models import TextRecord

def add_record(request):
    # Example text (hardcoded for URL-based access)
    record = TextRecord(content="Hello from /add endpoint")
    record.save()
    return HttpResponse("Record successfully added to the database.")
```

✔ Inserts data via **browser URL access**

---

# 6️⃣ Implement the `/show` View (Retrieve Records)

Add this to `views.py`:

```python
def show_records(request):
    records = TextRecord.objects.all()
    output = "<br>".join([r.content for r in records])
    return HttpResponse(output)
```

✔ Retrieves and displays **all stored records**

---

# 7️⃣ Configure App URL Routing

Create `textapp/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_record),
    path('show', views.show_records),
]
```

---

# 8️⃣ Connect App URLs to Project URLs

Open `textproject/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('textapp.urls')),
]
```

✔ URL routing is now properly configured

---

# 9️⃣ Run the Server

```bash
python manage.py runserver
```

---

# 🔍 How to Test (Critical for Validation)

### 1️⃣ Insert data

Open browser:

```
http://127.0.0.1:8000/add
```

✔ You should see:

```
Record successfully added to the database.
```

### 2️⃣ Retrieve data

Open:

```
http://127.0.0.1:8000/show
```

✔ You should see:

```
Hello from /add endpoint
```

Refresh `/add` multiple times → `/show` will list multiple records.

---

# ✅ Requirement Checklist (Mapped Exactly)

| Requirement                  | Status |
| ---------------------------- | ------ |
| Database configured          | ✔      |
| Model with text-based table  | ✔      |
| Database migrations          | ✔      |
| `/add` inserts data          | ✔      |
| `/show` retrieves data       | ✔      |
| Proper URL routing           | ✔      |
| HTTP-triggered DB read/write | ✔      |

---
