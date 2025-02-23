# htop-django
# Morphle Labs Assignment
A Django-based web application that displays system process information using htop (on Linux) or tasklist (on Windows).

# Features
Displays system process information.
Shows server time in IST (Asia/Kolkata).
Detects the current username dynamically based on OS.
Supports both Linux/macOS (htop) and Windows (tasklist).

# Tech Stack
Backend: Django 5.1
Python Modules: subprocess, datetime, pytz, os
Frontend: Basic HTML response from Django views.

# Available Routes

| Endpoint   | Description                  |
|------------|------------------------------|
| `/`        | Homepage                     |
| `/htop/`   | Displays system processes    |
| `/admin/`  | Django Admin Panel           |


![Screenshot 2025-02-22 150745](https://github.com/user-attachments/assets/4848afd7-d11e-4e6b-9753-9a6313164f5e)
