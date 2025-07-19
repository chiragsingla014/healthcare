# Healthcare Backend System

This project is a robust backend system for a healthcare application, built with Django and Django REST Framework. It provides a secure, scalable foundation for managing user authentication, patient records, and doctor information.

The live, interactive API documentation can be found here: **[Link to your live Swagger/Redoc Documentation]**

## Features

* **User Authentication**: Secure user registration and login using JSON Web Tokens (JWT).
* **Patient Management**: Full CRUD (Create, Read, Update, Delete) functionality for patient records, accessible only by the authenticated user who created them.
* **Doctor Management**: Full CRUD functionality for doctor records.
* **Patient-Doctor Mapping**: Ability to assign doctors to patients and manage these relationships.
* **Secure Endpoints**: Patient-related endpoints are protected, ensuring users can only access their own data.
* **Scalable Architecture**: Built following best practices for a clean and maintainable project structure.

## Tech Stack

* **Backend**: Django, Django REST Framework (DRF)
* **Database**: PostgreSQL
* **Authentication**: djangorestframework-simplejwt
* **Web Server**: Gunicorn
* **API Documentation**: drf-spectacular (Swagger/Redoc)
* **Environment Variables**: python-decouple

## API Documentation

All API endpoints are documented using Swagger UI. The interactive documentation details all available endpoints, required parameters, request/response schemas, and allows for live API testing.

**Access the API Documentation:** 
(This is deployed on a free tier, so the first visit may take a moment due to a cold start.)

**https://healthcare-slox.onrender.com/api/docs/**

---

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.8+
* PostgreSQL
* Pip for package management

### Local Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/chiragsingla014/healthcare
    
    ```

2.  **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    cd healthcare_backend
    ```

3.  **Set up the PostgreSQL Database:**
    * Create a new PostgreSQL database.
    * Note the database name, user, and password.

4.  **Configure Environment Variables:**
    * Create a `.env` file in the root directory of the project.

    ```env
    SECRET_KEY='your-django-secret-key'
    DEBUG=True
    DATABASE_URL='your-db-url'
    ```

### Running the Application

1.  **Apply database migrations:**
    ```sh
    python manage.py migrate
    ```

2.  **Start the development server:**
    ```sh
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000`.

## Testing

Unit tests have been implemented for the authentication endpoints to ensure reliability.

To run the tests, execute the following command:
```sh
python manage.py test users
```

## Project Structure

The project follows a standard Django application structure to ensure maintainability and scalability.

```
healthcare_backend/
├── healthcare_backend/
├── users/               # App for User models, authentication 
├── records/            # App for Patient, Doctors and thier mapping models and APIs
├── manage.py
└── .env

```
