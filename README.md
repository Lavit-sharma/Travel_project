
# Travel Booking Django Project

A simple travel booking web application built using Django and MySQL.

---

## Features

- User registration and login
- View and book travel options
- User-specific bookings page
- Clean and responsive UI with Bootstrap

---

## Requirements

- Python 3.9 or higher  
- MySQL server installed and running  
- pip (Python package installer)  
- Virtual environment tool (recommended)

---

## Setup Instructions (Local Development)

### 1. Clone the repository

git clonehttps://github.com/Lavit-sharma/Travel_project.git
cd repository-name



### 2. Create and activate a virtual environment

python -m venv venv

Windows
venv\Scripts\activate

macOS/Linux
source venv/bin/activate


### 3. Install dependencies

pip install -r requirements.txt


### 4. Create a `.env` file in the project root

Add the following environment variables (modify values to your setup):

MYSQL_DB_NAME=travel_db
MYSQL_USER=your user
MYSQL_PASSWORD=your password
MYSQL_HOST=localhost
MYSQL_PORT=your port
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1


### 5. Setup the MySQL database

Make sure your MySQL server is running and create the database:

CREATE DATABASE travel_db;


### 6. Apply migrations

python manage.py migrate


### 7. Run the development server

python manage.py runserver

Open your browser and visit `http://127.0.0.1:8000/` to see the application in action.

---

## Important Notes

- Never commit your `.env` file or any file containing sensitive credentials to version control.  
- The `.env` file is included in `.gitignore` to prevent accidental commits.  
- Set `DJANGO_DEBUG=False` in production environments.  
- Customize `ALLOWED_HOSTS` according to your deployment environment.

---

## Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes.

---

## Contact

For any questions or support, contact: [Your Email Address]

---
