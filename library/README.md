# DJANGO LIBRARY MANAGEMENT APP
    This application is a web application that allows you to manage a library's collection of books. With this app, you can view, add, edit, and delete books and students, as well as issue books to students.

## Features
    - Add new books to the library collection
    - Add new students to the library database
    - Edit existing book information
    - Edit existing student information
    - Delete books from the collection
    - Delete students from the database
    - Search for books by title
    - View details about each book
    - Issue books to students
    - View a list of all students and the books they have checked out

## Installation

    1. Clone the repository:
    ```
    https://github.com/MinjonH/django-library.git
    ```

    2. Start a virtual environment:
    ```
    python -m venv [virtualenv name]
    venv\scripts\activate
    ```

    3. Install the requirements:
    ```
    pip install -r requirements.txt
    ```

    4. Create the database:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

    5. Create a superuser
    ```
    python manage.py createsuperuser

    6. Run the development server:
    ```
    python manage.py runserver
    ```

## Usage
    To use the Django Library Management App, go to http://localhost:8000 in your web browser. You will be prompted to log in as a superuser.

    Once logged in, you can add, edit, and delete books from the library, as well as manage students and book issues.

## Running the app with Docker

    1. Go to [https://labs.play-with-docker.com/] (https://labs.play-with-docker.com/) and login with your Docker Hub account. If you do not have an account, create one here [https://hub.docker.com/] (https://hub.docker.com/)

    2. Then click “Start”, and on the next screen click “add new instance”.

    3. In the terminal, issue the following command to automatically download and run the Docker image:
    ```
    docker run -d -p 80:80 minjonh/django-library
    ```

    4. When the run command is done, you should see a button with the number “80” next to “OPEN PORT” at the top of the webpage. Click on it to visit your website on port 80.