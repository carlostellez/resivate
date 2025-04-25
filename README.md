# Resivate

A FastAPI project for resivate, developed with Python 3.13 with MySQL database integration.

## Features

- Modern FastAPI framework
- Python 3.13 compatibility
- Clean architecture with dependency injection
- MySQL database integration with SQLAlchemy ORM
- API documentation with OpenAPI specification
- Category management API with CRUD operations
- Image management API with CRUD operations

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Configure your MySQL database in `.env` file (see [Configuration](#configuration))
4. Run database migrations:
```bash
python create_tables.py
```

## Configuration

Create a `.env` file in the root directory with the following content:

```
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_SERVER=localhost
MYSQL_PORT=3306
MYSQL_DB=resivate_db
```

## Development

Start the development server:
```bash
PYTHONPATH=$PWD uvicorn app.main:app --reload
```

Access the API documentation at `http://localhost:8000/docs`

## Testing

Run tests:
```bash
PYTHONPATH=$PWD pytest app/tests/
```

## Project Structure

```
resivate/
├── app/
│   ├── api/
│   │   └── endpoints/
│   │       ├── category.py
│   │       └── image.py
│   ├── core/
│   │   ├── config.py
│   │   └── deps.py
│   ├── database/
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   │   ├── category.py
│   │   └── image.py
│   ├── schemas/
│   │   ├── category.py
│   │   └── image.py
│   ├── docs/
│   │   ├── openapi.yml
│   │   └── openapi_image.yml
│   ├── tests/
│   │   ├── test_category.py
│   │   └── test_image.py
│   └── main.py
├── alembic/
│   ├── versions/
│   └── env.py
├── alembic.ini
├── create_tables.py
├── README.md
├── pyproject.toml
└── requirements.txt
```

## API Endpoints

### Category API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/categories` | List all categories |
| GET | `/api/categories/{id}` | Get a category by ID |
| POST | `/api/categories` | Create a new category |
| PUT | `/api/categories/{id}` | Update a category |
| DELETE | `/api/categories/{id}` | Delete a category |

### Image API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/images` | List all images |
| GET | `/api/images/{id}` | Get an image by ID |
| POST | `/api/images` | Create a new image |
| PUT | `/api/images/{id}` | Update an image |
| DELETE | `/api/images/{id}` | Delete an image |
