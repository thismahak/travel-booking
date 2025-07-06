
````markdown
# ✈️ Travel Booking

A full-featured Django-based travel booking application that allows users to easily browse and book flights, trains, and buses. The app includes secure user authentication, profile management, booking history, and a responsive UI.

---

## ✅ Features

- User registration & authentication  
- Profile update and logout  
- Browse travel options with filters (type, source, destination)  
- Book available travel routes (flights, trains, buses)  
- View and manage your bookings (cancel upcoming trips)  
- Contact form for inquiries  
- Mobile-friendly UI using Bootstrap 5  

---

## 🛠 Tech Stack

- **Backend:** Django 5.2  
- **Database:** MySQL  
- **Frontend:** HTML, CSS (Bootstrap 5)  
- **Templating:** Django Templates  
- **Others:** Django built in libraries/features,  decouple  

---

## ⚙️ Setup Instructions (Local Only)

### 🔐 Prerequisites

- Python 3.10+  
- MySQL Server  
- Git  

### 🧱 Clone the Repository

```bash
git clone https://github.com/thismahak/travel-booking.git
cd travel-booking
````

### 🧪 Create and Activate a Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 📦 Install Requirements

```bash
pip install -r requirements.txt
```

### ⚙️ Configure `.env` File

Create a `.env` file in the root directory with the following:

```env
SECRET_KEY=your-django-secret-key
DB_NAME=your-db-name
DB_USER=your-db-username
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=3306
```

### 🧮 Apply Migrations

```bash
python manage.py migrate
```

### 👤 Create Superuser (Admin Panel Access)

```bash
python manage.py createsuperuser
```

### 🚀 Start Development Server

```bash
python manage.py runserver
```

Visit: [http://localhost:8000](http://localhost:8000)

---

## 📌 Notes

* This project uses **python-decouple** to manage environment variables.
* MySQL must be running locally and user credentials must have permissions for the specified database.
* Deployment is **not included** due to paid restrictions on Railway with MySQL.

---

## 🧪 Run Tests

```bash
python manage.py test
```

---

## 📂 Directory Structure (Simplified)

```
travel_booking/
├── core/                 # Main app (views, models, forms)
    ├── templates/            # All HTML templates
    ├── templatetags/
    ├── tests/               # some units tests for critical features 
├── travel_booking/       # Project settings
├── requirements.txt
├── .env
└── manage.py
└── sql.sql

```

---

## 📄 License

MIT License — free to use and modify.

---

## 🙋 Contact

For queries or suggestions, reach out via [GitHub Issues](https://github.com/thismahak/travel-booking/issues).

```

---

---

## 📸 Screenshots

You can see them in travel-booking/screenshots/



Happy coding! 🚀
```
