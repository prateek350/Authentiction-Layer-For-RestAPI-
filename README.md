# Authentiction-Layer-For-RestAPI-

FastAPI authentication service with a modular backend structure for user signup and login.

## Run locally

1. Install Python 3.11+.
2. Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set environment variables in `backend/.env`:

```env
PG_USERNAME=postgres
PG_PASSWORD=postgres
PG_HOST=localhost
PG_PORT=5432
PG_DB=authentication_db
SECRET_KEY=replace-this-secret
```

5. Start the API from the repo root:

```bash
uvicorn backend.src.main:app --reload
```

## API routes

- `GET /` health-style root endpoint
- `POST /api/users/` create a user
- `POST /api/login` obtain a bearer token
