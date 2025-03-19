# YNAB-Venmo Integration Backend

This is the backend service for the YNAB-Venmo integration application. It enables automatic syncing of Venmo transactions to YNAB by processing forwarded Venmo transaction emails.

## How it Works

1. Users forward their Venmo transaction emails to a designated email address
2. SendGrid receives the emails and sends webhooks to this backend
3. The backend parses the Venmo transaction details from the emails
4. Transactions are stored in a Supabase database
5. The backend batches and sends the transactions to the YNAB API

## Technology Stack

- **Framework**: FastAPI
- **Database ORM**: SQLAlchemy
- **Migration Tool**: Alembic
- **Python Version**: 3.x
- **Database**: PostgreSQL (via Supabase)
- **Deployment**: Render

## Project Structure

```
backend/
├── app/                    # Main application directory
│   ├── api/               # API routes and endpoints
│   ├── core/              # Core functionality and utilities
│   ├── models.py          # Database models
│   ├── database.py        # Database configuration
│   └── config.py          # Application configuration
├── migrations/            # Database migrations
├── .env                   # Environment variables
├── alembic.ini           # Alembic configuration
├── main.py               # Application entry point
├── requirements.txt      # Project dependencies
└── render.yaml           # Deployment configuration
```

## Setup and Installation

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your `.env` file with the necessary environment variables

4. Initialize the database:
   ```bash
   alembic upgrade head
   ```

## Environment Setup

1. Copy the `.env.example` file to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Fill in the following environment variables in your `.env` file:
   - **Supabase Configuration**:
     - `SUPABASE_URL`: Your Supabase project URL
     - `SUPABASE_KEY`: Supabase anon key
     - `SUPABASE_PWD`: Database password
     - `DATABASE_URL`: Supabase connection string
     - `SUPABASE_JWT_KEY`: JWT secret key

## Development Workflow

### Running the Application Locally

```bash
fastapi dev main.py
```

### Database Migrations

When making changes to the database schema:

1. Update your models in `app/models.py`
2. Generate a new migration:
   ```bash
   alembic revision --autogenerate -m "Description of change"
   ```
3. Review the generated migration in `migrations/versions/`
4. Apply the migration:
   ```bash
   alembic upgrade head
   ```
5. Commit all changes to git


## Deployment

The application is deployed on Render.com. The deployment configuration is specified in `render.yaml`. The service automatically builds and deploys when changes are pushed to the main branch.

Deployment configuration includes:
- Runtime: Python
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

## Testing and Verification

### Local Testing
1. Start the development server:
   ```bash
   fastapi dev main.py
   ```

2. Access the API documentation at `http://localhost:8000/docs`
   - The Swagger UI provides interactive documentation for all endpoints
   - You can test endpoints directly from the browser

### Integration Testing
1. **Frontend Connection Test**:
   - Navigate to `/protected/test` in the frontend application
   - This endpoint verifies the connection between frontend and backend

2. **Database Verification**:
   - Check Supabase to verify data is being properly stored
   - Monitor transaction records after processing emails

3. **API Testing with Bruno**:
   - Use Bruno to test individual endpoints
   - Verify webhook processing
   - Test transaction batching and YNAB integration

## API Documentation

FastAPI automatically generates interactive API documentation using Swagger UI. To access it:

1. Start the server (if running locally)
2. Navigate to `/docs` endpoint
3. The documentation includes:
   - All available endpoints
   - Request/response schemas
   - Authentication requirements
   - Interactive testing interface

