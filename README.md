# UGAS Pilates

A Django web application for managing Pilates studio operations, including class
scheduling, student management, and payment processing.

## Features

- Class scheduling and management
- Student registration and profiles
- Payment processing and tracking
- Instructor management
- Attendance tracking
- Content management with TinyMCE editor
- File management with FileBrowser

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ugas_pilates.git
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create and configure environment settings:

Create a `.env` file in the project root with the following structure:

```
DJANGO_ENV=development
DJANGO_SETTINGS_MODULE=ugas_pilates.settings.dev
DEBUG=True
SECRET_KEY=your-secret-key-here

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
ALLOWED_HOSTS=127.0.0.1,localhost

GM_KEY=your-google-maps-api-key
```

Note: This is a personal project for managing a specific Pilates studio. You'll
need to set up your own environment variables and database configuration if you
want to run it.

5. Run migrations:

```bash
python manage.py migrate
```

6. Create a superuser:

```bash
python manage.py createsuperuser
```

7. Start the development server:

```bash
python manage.py runserver
```

## Usage

1. Access the application at `http://localhost:8000`
2. Log in with your superuser credentials

## Technologies

- Backend Framework: Django
- Database: PostgreSQL
- Admin Interface: Grappelli
- Rich Text Editor: TinyMCE
- File Management: FileBrowser
- Development Tools: Django Debug Toolbar

## License

MIT License - see LICENSE file for details.
