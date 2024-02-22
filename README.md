# Apexive

Apexive is a Django-based project designed to manage aircraft and flight data. It includes functionalities for importing data from JSON files into the database and exporting data to CSV files. This guide will help you set up and get started with the Apexive project on your local machine.

## Prerequisites

Before you start, ensure you have the following installed:

- **Python 3.10.6**: The project is tested with Python 3.10.6. We recommend using `pyenv` for easy Python version management.
  - **Linux**: [Follow the guide here](https://realpython.com/intro-to-pyenv/#installing-pyenv) to install Python with `pyenv` on Linux.
  - **Mac OS**: For Mac OS installation instructions, [visit this page](https://github.com/pyenv/pyenv#installation).
- **Pipenv**: This project uses `Pipenv` for dependency management and virtual environment setup.
  - **Mac OS**: Run `brew install pipenv`.
  - **Linux**: Execute `pip install --user pipenv`.

## Setup

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd <project-directory>
```

### Initialize the Environment

Activate the `pipenv` shell to create a virtual environment for the project:

```bash
pipenv shell
```

Install all the dependencies specified in `Pipfile.lock`:

```bash
pipenv install
```

### Database Migrations

Before running the server, apply the database migrations to set up your database schema:

```bash
python manage.py migrate
```

### Run the Development Server

To start the Django development server, run:

```bash
python manage.py runserver
```

This command will start the server on http://127.0.0.1:8000/, where you can access the API endpoints.

## Using the Project

### Import Data Module

To import data from a JSON file into the database, execute:

```bash
python manage.py import_data
```

### Export Data Module

To export aircraft or flight data to a CSV file, run:

```bash
python manage.py export_data
```

### Accessing API Endpoints

With the server running, you can access the following API endpoints:

- **List Aircraft**: `GET /api/aircraft/`
- **Retrieve Aircraft**: `GET /api/aircraft/<aircraft_id>/`
- **List Flights**: `GET /api/flights/`
- **Retrieve Flight**: `GET /api/flights/<flight_guid>/`

You can use tools like `curl` or Postman to make requests to these endpoints or access them directly from your web browser.

## Testing

To run the automated test suite and ensure everything is working as expected, execute:

```bash
python manage.py test
```

This command will discover and run all tests defined in the tests directory of the app.

## Additional Commands

### Create a Superuser

To access the Django admin interface, you may need to create a superuser account:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the username, email, and password for the superuser
