# URL Shortener API

A RESTful API for creating and managing shortened URLs, built with FastAPI and PostgreSQL. Supports full CRUD operations and tracks access statistics per short URL.

## Features

- Generate unique short codes for long URLs
- Retrieve, update, and delete existing short URLs
- Track how many times each short URL has been accessed
- Input validation and structured error responses via Pydantic
- Persistent storage with PostgreSQL

## Tech Stack

- **FastAPI** — API framework with automatic request validation and interactive docs
- **PostgreSQL** — relational database for persistent storage
- **SQLAlchemy** — ORM for database modeling and query abstraction
- **Pydantic** — schema definition and request/response validation
- **python-dotenv** — environment variable management

## Project Structure

```
url-shortener/
├── main.py          # App entry point, route definitions
├── database.py      # SQLAlchemy engine and session setup
├── models.py        # Database table definition
├── schemas.py       # Pydantic request/response schemas
├── crud.py          # Database operations
├── .env             # Environment variables (not committed)
└── requirements.txt
```

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/betancourt-ncs/url-shortener-API.git
cd url-shortener
```

**2. Create and activate a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up PostgreSQL**

Create a local database:
```bash
psql postgres
CREATE DATABASE url_shortener;
\q
```

**5. Configure environment variables**

Create a `.env` file in the project root:
```
DATABASE_URL=postgresql://your_username@localhost:5432/url_shortener
```

**6. Run the server**
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.
Interactive docs are available at `http://127.0.0.1:8000/docs`.

## API Reference

### Create Short URL
```
POST /shorten
```
**Request body:**
```json
{
  "url": "https://www.example.com/some/long/url"
}
```
**Response `201`:**
```json
{
  "id": 1,
  "url": "https://www.example.com/some/long/url",
  "shortCode": "abc123",
  "created_at": "2021-09-01T12:00:00Z",
  "updated_at": "2021-09-01T12:00:00Z"
}
```

---

### Retrieve Original URL
```
GET /shorten/{short_code}
```
**Response `200`:** Returns the URL object for the given short code.
**Response `404`:** Short URL not found.

---

### Update Short URL
```
PUT /shorten/{short_code}
```
**Request body:**
```json
{
  "url": "https://www.example.com/updated/url"
}
```
**Response `200`:** Returns the updated URL object.
**Response `404`:** Short URL not found.

---

### Delete Short URL
```
DELETE /shorten/{short_code}
```
**Response `204`:** Short URL successfully deleted.
**Response `404`:** Short URL not found.

---

### Get URL Statistics
```
GET /shorten/{short_code}/stats
```
**Response `200`:**
```json
{
  "id": 1,
  "url": "https://www.example.com/some/long/url",
  "shortCode": "abc123",
  "created_at": "2021-09-01T12:00:00Z",
  "updated_at": "2021-09-01T12:00:00Z",
  "accessCount": 10
}
```
**Response `404`:** Short URL not found.

## Reflection

This project solidified my understanding of RESTful API design and working with relational databases in a production-like setup. Key concepts I worked through include CRUD architecture, SQLAlchemy ORM modeling, request/response validation with Pydantic, dependency injection, and clean separation of concerns across a multi-file backend.

For more info visit https://roadmap.sh/projects/url-shortening-service


## License

MIT
