# Django CBV ToDoApp CRUD

A simple ToDo application built using Django, demonstrating the use of class-based views (CBVs) for implementing CRUD (Create, Read, Update, Delete) operations. This application allows users to manage tasks through a user-friendly interface, with full functionality for adding, viewing, editing, and deleting tasks.

## Features

- **Create Tasks**: Add new tasks with a title and description.
- **Read Tasks**: View a list of tasks with their details.
- **Update Tasks**: Edit an existing task's title and description.
- **Delete Tasks**: Remove tasks from the list.
- **Class-Based Views**: Implements CRUD operations using Django's CBVs for better modularity and reuse.

## Requirements

- **Python 3.x**
- **Django**: The main framework used for the project.
- **SQLite** (default database for Django, can be replaced with PostgreSQL or MySQL).

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/shahramsamar/Django_Cbv_ToDoApp_CRUD.git
    cd Django_Cbv_ToDoApp_CRUD
    ```

2. **Install Dependencies:**

    If you're using `pip`, run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Apply Migrations**:

    Run the following command to set up the database schema:

    ```bash
    python manage.py migrate
    ```

4. **Create a Superuser (Admin)**:

    To manage tasks via the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

5. **Run the Development Server**:

    Start the development server with:

    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000/`.

### How to Use

- **Access the To-Do List**: Visit the home page to see the list of tasks.
- **Add a Task**: Click the "Add Task" button to create a new task with a title and description.
- **Edit a Task**: Click the "Edit" button next to a task to update its details.
- **Delete a Task**: Click the "Delete" button next to a task to remove it from the list.
- **Admin Panel**: You can also manage tasks from the Django admin panel at `http://127.0.0.1:8000/admin/`.

### Project Structure

- `todo/`: The main app that contains the ToDo functionality.
    - `models.py`: Defines the Task model with `title` and `description`.
    - `views.py`: Contains class-based views for creating, reading, updating, and deleting tasks.
    - `urls.py`: Routes the URLs for the task-related views.
    - `forms.py`: Defines the form for adding and editing tasks.
    - `templates/`: Stores HTML templates for rendering the views.
        - `task_list.html`: Displays the list of tasks.
        - `task_form.html`: The form used for creating or editing tasks.
    - `static/`: Contains any static files (CSS, JavaScript).
- `requirements.txt`: Lists all dependencies for the project (e.g., Django).
- `manage.py`: The Django project management script for running the application.

### Contributing

Feel free to fork the project and submit pull requests for new features, improvements, or bug fixes.

### License

This project is open-source and available for educational purposes.

---

This `README.md` provides detailed instructions for setting up, using, and contributing to the **Django CBV ToDoApp CRUD** project. It covers installation, usage, and how to interact with the ToDo application using class-based views.
![Alt](https://repobeats.axiom.co/api/embed/eabe6508a91fa38b4ace0060919094363916f544.svg "Repobeats analytics image")
