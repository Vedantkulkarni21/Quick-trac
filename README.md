# QuickTrac - A practice project

A full-stack Product Management CRUD application built using React, FastAPI, SQLAlchemy, and MySQL.

## Features

- Create, Read, Update, Delete (CRUD) products
- FastAPI REST APIs
- MySQL database integration
- SQLAlchemy ORM
- React frontend with Axios
- Product search and filtering
- Sorting functionality
- Edit and delete operations
- Responsive UI

## Tech Stack

### Frontend
- React.js
- Axios
- CSS

### Backend
- FastAPI
- SQLAlchemy
- Pydantic
- PyMySQL

### Database
- MySQL

---

# Project Structure

```bash
backend/
│
├── main.py
├── models.py
├── database.py
├── database_models.py
└── requirements.txt

frontend/
│
├── src/
├── public/
└── package.json
```

---

# Backend Setup

## 1. Create Virtual Environment

```bash
python -m venv venv
```

## 2. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run FastAPI Server

```bash
uvicorn main:app --reload
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

---

# Frontend Setup

## 1. Install Dependencies

```bash
npm install
```

## 2. Start React App

```bash
npm start
```

Frontend runs on:

```bash
http://localhost:3000
```

---

# API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/products` | Get all products |
| GET | `/products/{id}` | Get product by ID |
| POST | `/products` | Add product |
| PUT | `/products/{id}` | Update product |
| DELETE | `/products/{id}` | Delete product |

---

# Future Improvements

- JWT Authentication
- User login/signup
- Docker deployment
- Pagination
- Image upload support
- Cloud deployment (AWS/GCP)

---

# Author

Vedant Kulkarni
