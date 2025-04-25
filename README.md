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
- FAQ management API with CRUD operations
- Menu Options management API with CRUD operations (supporting complex JSON arrays)
- Service Types management API with CRUD operations
- Custom SQLAlchemy hybrid property serialization for complex JSON data types

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

### Handling Complex JSON Data

The project includes a custom implementation for handling complex JSON data in SQLAlchemy models:

1. The `MenuOption` model demonstrates how to store and retrieve complex JSON arrays using hybrid properties
2. The `Type` model stores feature lists as JSON strings with proper serialization/deserialization
3. A custom `__getattribute__` method ensures correct serialization when FastAPI accesses model attributes
4. Pydantic schemas with proper typing ensure validation and serialization of complex nested structures

This approach allows you to work with arrays and nested JSON objects in MySQL (which doesn't natively support arrays) while maintaining type safety and ORM capabilities.

#### Simple Array Example

```python
# Create a simple menu option with string array items
menu_option = {
    "type": "Restaurants",
    "items": ["Coffee shops", "Full service"]
}
```

#### Features List Example

```python
# Create a service type with a features list
service_type = {
    "title": "Premium Service",
    "description": "Our top-tier service offering",
    "features": ["24/7 Support", "Priority Response", "Custom Solutions"]
}
```

## Testing

Run tests:
```bash
PYTHONPATH=$PWD pytest app/tests/
```

### Code Coverage

Generate code coverage report:
```bash
PYTHONPATH=$PWD pytest --cov=app app/tests/
```

For a detailed HTML report:
```bash
PYTHONPATH=$PWD pytest --cov=app --cov-report=html app/tests/
```

This will create a `htmlcov` directory with HTML coverage reports. Open `htmlcov/index.html` in a browser to view the coverage results.

## Project Structure

```
resivate/
├── app/
│   ├── api/
│   │   └── endpoints/
│   │       ├── category.py
│   │       ├── image.py
│   │       ├── faq.py
│   │       ├── menu_option.py
│   │       ├── option.py
│   │       └── plan.py
│   ├── core/
│   │   ├── config.py
│   │   └── deps.py
│   ├── database/
│   │   ├── base.py
│   │   ├── base_class.py
│   │   └── session.py
│   ├── models/
│   │   ├── category.py
│   │   ├── image.py
│   │   ├── faq.py
│   │   ├── menu_option.py
│   │   ├── option.py
│   │   └── plan.py
│   ├── schemas/
│   │   ├── category.py
│   │   ├── image.py
│   │   ├── faq.py
│   │   ├── menu_option.py
│   │   ├── option.py
│   │   ├── plan.py
│   │   └── type.py
│   ├── docs/
│   │   ├── openapi.yml
│   │   ├── openapi_image.yml
│   │   ├── openapi_faq.yml
│   │   ├── openapi_menu_option.yml
│   │   ├── openapi_option.yml
│   │   ├── openapi_plan.yml
│   │   └── openapi_type.yml
│   ├── tests/
│   │   ├── test_category.py
│   │   ├── test_image.py
│   │   ├── test_faq.py
│   │   ├── test_menu_option.py
│   │   ├── test_option.py
│   │   ├── test_plan.py
│   │   └── test_type.py
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

### FAQ API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/faqs` | List all FAQs |
| GET | `/api/faqs/{id}` | Get a FAQ by ID |
| POST | `/api/faqs` | Create a new FAQ |
| PUT | `/api/faqs/{id}` | Update a FAQ |
| DELETE | `/api/faqs/{id}` | Delete a FAQ |

### Menu Options API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/menu-options` | List all menu options |
| GET | `/api/menu-options/{id}` | Get a menu option by ID |
| POST | `/api/menu-options` | Create a new menu option |
| PUT | `/api/menu-options/{id}` | Update a menu option |
| DELETE | `/api/menu-options/{id}` | Delete a menu option |

#### Example Menu Option

```json
{
  "type": "Restaurants",
  "items": ["Coffee shops", "Full service"]
}
```

This simple array-based menu option can be used to display a list of options for the "Restaurants" category.

### Options API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/options` | List all options |
| GET | `/api/options/{id}` | Get an option by ID |
| POST | `/api/options` | Create a new option |
| PUT | `/api/options/{id}` | Update an option |
| DELETE | `/api/options/{id}` | Delete an option |

#### Example Option

```json
{
  "name": "Configuration",
  "icon": "settings"
}
```

This option structure provides a name and icon pair that can be used for UI elements such as configuration options, settings, or menu items.

### Plans API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/plans` | List all pricing plans |
| GET | `/api/plans/{id}` | Get a pricing plan by ID |
| POST | `/api/plans` | Create a new pricing plan |
| PUT | `/api/plans/{id}` | Update a pricing plan |
| DELETE | `/api/plans/{id}` | Delete a pricing plan |

#### Example Plan

```json
{
  "title": "Basic Plan",
  "description": "Basic features for small businesses",
  "price": 19.99,
  "btnMessage": "Get Started",
  "blueBtn": true
}
```

This plan structure provides pricing information with customizable button options. The `blueBtn` property allows for styling distinctions between different plan types.

### Types API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/types` | List all service types |
| GET | `/api/types/{id}` | Get a service type by ID |
| POST | `/api/types` | Create a new service type |
| PUT | `/api/types/{id}` | Update a service type |
| DELETE | `/api/types/{id}` | Delete a service type |

#### Example Type

```json
{
  "title": "Service Type",
  "description": "Description of service type",
  "features": ["Feature 1", "Feature 2", "Feature 3"],
  "img_id": 1,
  "img": {
    "id": 1,
    "src": "https://example.com/image.jpg"
  }
}
```

This type structure includes a title, description, and an array of features. It also supports an optional relationship with an image, allowing service types to be visually represented.
