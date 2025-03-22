# Password Generator Django App

## Overview

This is a simple Django-based password generator web application that allows users to generate strong passwords of a specified length. The app provides a REST API for password generation and a web interface for easy interaction.

## Features

* Generates secure passwords containing lowercase, uppercase, digits, and special characters.
* Simple web UI using Bootstrap for a responsive design.
* Password copy-to-clipboard feature.
* Auto-hide generated password after 7 seconds.
* Health check endpoint to verify application status.

## Installation

### Prerequisites

Ensure you have the following installed:

* Python (>=3.7)
* Django (>=3.0)
* Virtual environment (optional but recommended)

### Steps

1.  **Clone the Repository:**

    ```bash
    git clone <repository-url>
    cd password_generator_app
    ```

2.  **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # On Windows use: venv\Scripts\activate
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Migrations (if needed):**

    ```bash
    python manage.py migrate
    ```

5.  **Start the Django Server:**

    ```bash
    python manage.py runserver
    ```

6.  **Access the Web UI:**

    Open a browser and go to:

    ```
    [invalid URL removed]
    ```

## API Endpoints

| Endpoint                              | Method | Description                                                                 |
| ------------------------------------- | ------ | --------------------------------------------------------------------------- |
| `/api/generate-password/?length=<number>` | GET    | Generates a random password with specified length (default: 8)              |
| `/api/health-check/`                  | GET    | Returns application health status and current IST time                      |

## Usage

### Web Interface

1.  Open the app in a browser.
2.  Enter the desired password length.
3.  Click "Generate" to get a secure password.
4.  Use the "Copy to Clipboard" button to copy the password.

### API Example

**Request:**

```bash
curl -X GET "[http://127.0.0.1:8000/api/generate-password/?length=12](http://127.0.0.1:8000/api/generate-password/?length=12)"
```

**Response:**

```bash
{
    "password": "A7!bX3$kLp9%"
}
```
### File Structure

```bash
password_generator_app/
├── templates/
│   ├── password_generator_app/
│   │   ├── index.html
├── views.py
├── urls.py
├── manage.py
├── README.md
```

### Technologies Used
* Django - Backend Framework
* Bootstrap - Frontend Styling
* JavaScript - For UI Interactivity
* Python - Core Programming Language

### License
This project is licensed under the MIT License.

### Author
Developed by praveenkumarv-github