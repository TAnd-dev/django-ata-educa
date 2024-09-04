# Django ATA Educa

Django ATA Educa is a web application designed to provide an online learning platform. It allows users to browse courses, register for them, and track their progress. This project is built using Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design.

## Features

- **User Authentication**: Sign up, log in and log out.
- **Course Management**: Create, update, delete, and view courses.
- **Lesson Management**: Add lessons to courses with rich content.
- **Admin Interface**: Admins can manage courses, lessons, and users via Django’s admin interface.

## Technologies Used

- **Backend**: Django 5.x, Django Rest Framework
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default, can be replaced with PostgreSQL or MySQL)
- **Other**: Docker for containerization, Nginx as a web server, uWSGI for serving Django applications.

## Installation

### Prerequisites

- Python 3.8+
- Docker and Docker Compose
- Git

### Local Development

1. **Clone the repository:**

   ```bash
   git clone https://github.com/TAnd-dev/django-ata-educa.git
   cd django-ata-educa

2. **Create a virtual environment and activate it:**

   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the dependencies:**

    ```bash
      pip install -r requirements.txt
    
4. **Run migrations:**

    ```bash
    python manage.py migrate

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser

6. **Run the development server:**

    ```bash
    python manage.py runserver --settings=base.settings.local_settings  # Or --settings=base.settings.prod_settings
    
The application will be available at http://127.0.0.1:8000/.

### Docker Setup
1. **Build and start the containers:**

    ```bash
    docker-compose up --build

2. **Access the application:**

The application will be available at http://localhost/

Admin interface: http://localhost/admin/

API root: http://localhost/api/
