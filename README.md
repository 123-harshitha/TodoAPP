# TODO App

A simple and user-friendly **TODO application** built with **Django**. This application allows users to manage their tasks efficiently by adding, updating, marking as completed, and deleting tasks.

## Features

- **User Authentication**: Allows users to register, log in, and log out.
- **Task Management**: Users can add, update, and delete tasks.
- **Task Status**: Tasks can be marked as "completed" or "pending".
- **Responsive UI**: Built with HTML, CSS, and Django templates for a clean and responsive user interface.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS
- **Database**: SQLite (Django's default database; no additional setup required)
- **Version Control**: Git

## Setup and Installation

Follow these steps to set up and run the project locally:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/TODOApp.git
   cd TODOApp


2. Create a virtual environment (optional but recommended):
python3 -m venv venv
source venv/bin/activate  # For Windows, use `venv\Scripts\activate`


3 . Install the dependencies 
python
django 

4. Apply database migrations:
   python manage.py migrate

5. Run the development server:
    python manage.py runserver

6. Access the application in your browser
     Open your browser and go to http://127.0.0.1:8000/

Usage
Home Page: Displays a list of all tasks with options to mark as completed or delete.

Add Task: Users can add new tasks to their list.

Update Task: Users can edit the task description.

Mark as Completed: Users can mark tasks as completed to visually distinguish them from pending tasks.

Delete Task: Users can delete tasks that are no longer needed.


Folder Structure



todoApp/
├── todoApp/
│   └── todos/
│       ├── __pycache__/
│       ├── migrations/
│       ├── staticfiles/
│       └── templates/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── db.sqlite3
├── manage.py
└── req.txt

Requirements
Python 3.x

Django 3.x or above

License
This project is licensed under the MIT License - see the LICENSE file for details.

      
