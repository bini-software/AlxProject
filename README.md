# AlxProject
# Student Management API

This project is a simple API for managing **students, courses, and enrollments**. It is built with **Django** and **Django REST Framework (DRF)**. The API includes **authentication, role-based access control, filtering, ordering, and pagination**, so users can only access what they are allowed to.

---

## Project Overview (Flow)

The project structure is designed for clarity and separation of concerns:


---

## Features

### Students
- Admin can **create, list, update, and delete** students.
- Students can **view only their own information**.
- Supports **searching** (`?search=`), **ordering** (`?ordering=`), and **pagination** (`?page=`).

### Courses
- Admin can **create and manage courses**.
- Courses can be **listed and ordered**.

### Enrollments
- Admin can **create and manage enrollments**.
- Students can see only **their own enrollments**.
- Supports **searching** and **ordering** by student or course.

### Authentication & Permissions
- Token-based and session authentication are implemented.
- Role-based access control:
  - **Authenticated users** can create, update, or delete.
  - **List views** can be public or restricted depending on the role.

### Searching & Ordering
- Example search: `/api/students/?search=biniyam`
- Example ordering: `/api/students/?ordering=first_name`

---

## API Endpoints

### Students
- `GET /api/students/` — List students  
- `POST /api/students/` — Create student (Admin only)  
- `GET /api/students/<id>/` — Retrieve student details  
- `PUT /PATCH /api/students/<id>/` — Update student (Admin only)  
- `DELETE /api/students/<id>/` — Delete student (Admin only)  

### Courses
- `GET /api/courses/` — List courses  
- `POST /api/courses/` — Create course (Admin only)  
- `GET /api/courses/<id>/` — Retrieve course details  
- `PUT /PATCH /api/courses/<id>/` — Update course (Admin only)  
- `DELETE /api/courses/<id>/` — Delete course (Admin only)  

### Enrollments
- `GET /api/enrollments/` — List enrollments  
- `POST /api/enrollments/` — Create enrollment (Admin only)  
- `GET /api/enrollments/<id>/` — Retrieve enrollment details  
- `PUT /PATCH /api/enrollments/<id>/` — Update enrollment (Admin only)  
- `DELETE /api/enrollments/<id>/` — Delete enrollment (Admin only)  

### Authentication
- `POST /api/signup/` — Create a new user  
- `POST /api/login/` — Obtain authentication token  

---

## Installation

1. **Clone the project**
```bash
git clone https://github.com/bini-software/student_management_api.git
cd student_management_api

