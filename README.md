# getting-started-with-django

This project was built following the [JustDjango - Getting Started With Django Tutorial // Build a CRM](https://www.youtube.com/watch?v=fOukA4Qh9QA) tutorial on youtube. It's a complete 9 hours django tutorial where I lean how to create a project with Django and in the end, how to deploy it on Ocean Digital.

From this tutorial, I learn how to use and differentiate views based on function and classes, how to manage migrations, how to use the jinja template, which is amazing, and how to use crispy forms with the tailwind template.

I was always curious to start a project with Django because it provides a rich boilerplate to build web applications so easily. I'm very grateful to follow this complete tutorial, because with the concepts learned here, I intend to use in future projects.

## What Did I Learn?

* Migrations
* Difference between project and app
* Models
* Forms
* Relationships
* Querysets and Managers
* Django Admin Interface
* Function and class based views
* Context
* URL Namespaces
* Generic Views
* Templates
* Tailwind CSS
* Static files
* Send emails
* Tests
* Auth permissions (Middlewares)
* Signals
* Mixins
* Crispy forms
* Environment Variables
* Potgresql
* Whitenoise

## Libraries and tools used

* [Python 3.9](https://www.python.org/downloads/release/python-390/)
* [Django 3.1.4](https://docs.djangoproject.com/en/3.1/releases/3.1.4/)
* [Django Crispy Forms 1.11.2](https://django-crispy-forms.readthedocs.io/en/latest/)
* [Crispy Tailwind 0.4.0](https://github.com/django-crispy-forms/crispy-tailwind)
* [Django Environ 0.4.5](https://github.com/joke2k/django-environ)
* [Postgresql](https://www.postgresql.org/)
* [psycopg2-binary 2.8.6](https://pypi.org/project/psycopg2-binary/)
* [Whitenoise 5.2.0](http://whitenoise.evans.io/en/stable/django.html)

## Getting Started

### Install and configure PostgreSQL

1. Download and configure the PostgreSQL database.

2. Login as default user: `sudo -i -u postgres`.

3. Create a superuser:

    ```sql
    CREATE USER username WITH PASSWORD 'password';
    ```

4. Login with the user created and create a database.

    ```sql
    CREATE DATABASE database_name;
    ```

5. Grant all privileges to the user on the database created.

    ```sql
    GRANT ALL PRIVILEGES ON DATABASE database_name TO username;
    ```

6. You can verify these operation accessing the database created.

    ```
    psql -U username -h 127.0.0.1 database_name
    ```

### Install python dependencies

It's highly recommended that you create a virtual environment to install these dependencies. You can use [pipenv](https://pypi.org/project/pipenv/) or [venv](https://docs.python.org/pt-br/3/library/venv.html). Once you create the virtual environment (optional), you can install the dependencies in two ways:

1. Using pipenv:

    ```
    pipenv install
    ```

2. Using pip3:

    ```
    pip3 install -r requirements.txt
    ```
### Set environment variables

To run this project you will need to set your own environment variables.

1. Create a new file named .env inside the djcrm folder.

2. Copy all variables inside jdcrm/.template.env and assign your own values to them.

3. Run `export READ_DOT_ENV_FILE=True` inside your terminal, so that your environment variables file will be read.

### How to run

1. Run migrations:

    ```
    python manage.py migrate
    ```

2. Run the server:

    ```
    python manage.py runserver
    ```

3. Create a superuser:

    ```
    python manage.py createsuperuser
    ```
    This you create a user with super user privileges. You can access the Admin Dashboard on `http://127.0.0.1:8000/admin/`.

The server will be running on `http://127.0.0.1:8000/`

## TODO

- [ ] Add the number of leads assigned to each category.
- [ ] Use Mailgun on production.
- [ ] Deploy on Digital Ocean.
