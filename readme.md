
# 📚 QR-Based Event Check-In System

A backend system to manage college event registrations and event day check-ins using QR codes.  
Built with **FastAPI**, **MongoDB**, **JWT Authentication**, and **QR Code Generation**.

---

## 📌 Features

- 👤 **User Registration/Login** (Student/Admin roles)
- 🎟 **Event Creation** (Admin only)
- 🏫 **Student Event Registration**
- 🔲 **QR Code Generation** on registration
- 📧 **Email QR Code to users** (confirmation email)
- 📋 **Admin Dashboard**: View registered and checked-in users
- ✅ **Check-in system** via scanning QR code
- 📄 **Export attendee lists** (CSV/JSON)
- 🛡 **JWT Authentication** on protected routes
- 📜 **Swagger API Documentation** (auto generated)

---

## ⚙️ Tech Stack

| Layer | Technology |
|:------|:-----------|
| Backend | FastAPI (Python) |
| Database | MongoDB |
| Authentication | JWT (JSON Web Token) |
| QR Code | `qrcode` Python library |
| Emailing | `yagmail` (or SMTP) |
| Documentation | Swagger UI (built-in with FastAPI) |

---

## 🏗 Setup Instructions

1. **Clone the project**

```bash
git clone https://github.com/yourusername/qr-event-checkin.git
cd qr-event-checkin
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

(If `requirements.txt` is not created yet, install manually):
```bash
pip install fastapi uvicorn pymongo pydantic python-jose[cryptography] passlib[bcrypt] qrcode[pil] python-multipart yagmail
```

4. **Start MongoDB**

Make sure MongoDB is running locally or connect to a remote server.

5. **Run the server**

```bash
uvicorn app:app --reload
```

Server will start at:  
➡️ `http://127.0.0.1:8000`

---

## 🔑 Environment Variables

Create a `.env` file in your root folder (if needed) for:

```
MONGODB_URL=mongodb://localhost:27017
JWT_SECRET_KEY=your_jwt_secret_key
EMAIL_USER=your_email@example.com
EMAIL_PASSWORD=your_email_password
```

---

## 📚 API Endpoints Overview

| Method | Endpoint | Description |
|:------|:---------|:------------|
| POST | `/register` | User Registration (student/admin) |
| POST | `/login` | User Login (returns JWT) |
| POST | `/events/create` | Admin creates event |
| GET | `/events/` | View all events |
| POST | `/events/register/{event_id}` | Student registers for event (QR generated) |
| POST | `/events/checkin/{registration_id}` | Mark user as checked-in |
| GET | `/admin/dashboard` | View registered and checked-in users |

✅ **Swagger UI** available at:  
➡️ `http://127.0.0.1:8000/docs`

---

## 📦 Folder Structure

```
qr-event-checkin/
├── app.py             # Main FastAPI app
├── db.py              # MongoDB connection
├── auth.py            # JWT Authentication functions
├── models.py          # Pydantic models
├── routes/
│   ├── auth_routes.py
│   ├── event_routes.py
│   ├── admin_routes.py
├── utils/
│   ├── qr_generator.py
│   ├── email_sender.py
├── requirements.txt
├── README.md
```

---

## 💬 Future Improvements

- Admin panel with web interface
- QR Code scanning app
- OTP-based login (for higher security)
- More robust email templates

---

## 🧑‍💻 Author

- **[Chakshu Sharma]**
- [LinkedIn]([https://linkedin.com/in/yourprofile](https://www.linkedin.com/in/chakshu-sharma-6b151032a/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)) | [GitHub][(https://github.com/cshar21)}

- ## 📸 Screenshots

### 1. API Endpoints Overview
This shows all available API routes as generated by FastAPI's Swagger UI.

![API Endpoints](./screenshots/API%20Endpoints.png)

---

### 2. Authentication & Tags in Swagger UI
Demonstrates token-based auth and endpoint grouping by tags in the docs.

![API Tokens and Tags](./screenshots/API%20Tokens%20and%20Tags.png)

---

### 3. Application Running Locally
The backend successfully running on the local machine using Uvicorn.

![Application Running](./screenshots/Application%20Running.png)

---

### 4. Deployment on Render
Deployment process or log view from Render, confirming live status.

![Deployment Process](./screenshots/Deployment%20Process.png)
---

# 🚀 Let's build and check-in smartly!
