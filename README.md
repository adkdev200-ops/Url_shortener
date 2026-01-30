# Django URL Shortener

A simple and efficient URL shortening webservice built with Django. This application allows users to shorten long URLs, manage their links via a dashboard, and track click statistics.

## Features

- **User Authentication**: Secure Login, Sign Up, and Logout functionality.
- **URL Shortening**:
    - Convert long URLs into short, shareable links.
    - Option to provide a custom alias for your URL.
    - Auto-generate random aliases if none is provided.
- **Dashboard**:
    - View a list of all your shortened URLs.
    - Track the number of clicks for each link.
    - Delete unwanted links.
- **User Profile**:
    - Update user information (First Name, Last Name, Email).
    - Upload and update profile picture.
- **Redirection**: Seamlessly redirects users from the short URL to the original long URL.

## Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite (default)
- **Frontend**: HTML, CSS (Django Templates)

## Installation & Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd shortener
    ```

2.  **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**

    This project requires `Django` and `Pillow`.

    ```bash
    pip install django pillow
    ```

4.  **Apply Migrations:**

    Initialize the database setup.

    ```bash
    python manage.py migrate
    ```

5.  **Run the Server:**

    ```bash
    python manage.py runserver
    ```

6.  **Access the Application:**
    Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

1.  **Sign Up** for a new account.
2.  **Login** to access the home page.
3.  Enter a long URL and an optional alias in the form.
4.  Click **"Generate"** to create a short link.
5.  Go to the **Dashboard** to manage your links and view stats.
6.  Visit your short URL (e.g., `http://127.0.0.1:8000/<alias>`) to test the redirection.

## Project Structure

- `myapp/`: Contains the main application logic (models, views, etc.).
- `shortener/`: Project configuration settings and URLs.
- `templates/`: HTML templates for the frontend.
- `static/`: Static files (CSS, JS, Images).
- `media/`: User-uploaded content (Profile pictures).
