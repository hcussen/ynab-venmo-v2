# YNAB-Venmo Integration

Automatically import Venmo transactions into YNAB (You Need A Budget) by forwarding email notifications.

## Features

- Automatic processing of Venmo email notifications
- Direct integration with YNAB API
- User dashboard for transaction monitoring
- Error tracking and notification system

## Tech Stack

### Backend
- FastAPI (Python)
- PostgreSQL
- AWS SES for email processing
- YNAB API integration

### Frontend
- Next.js
- TypeScript
- Tailwind CSS

## Prerequisites

- Python 3.9+
- Node.js 18+
- PostgreSQL
- AWS Account (for SES)
- YNAB Developer Account
- Domain name for email receiving

## Project Structure

```
.
├── backend/              # FastAPI application
│   ├── app/
│   │   ├── api/         # API routes
│   │   ├── core/        # Core functionality
│   │   ├── db/          # Database models and migrations
│   │   ├── services/    # Business logic
│   │   └── utils/       # Utility functions
│   ├── tests/           # Backend tests
│   └── requirements.txt  # Python dependencies
│
├── frontend/            # Next.js application
│   ├── src/
│   │   ├── app/        # Next.js app directory
│   │   ├── components/ # React components
│   │   └── lib/        # Utility functions
│   └── package.json    # Node.js dependencies
│
└── docker/             # Docker configuration
```

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ynab-venmo-v2.git
cd ynab-venmo-v2
```

2. Backend setup:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Frontend setup:
```bash
cd frontend
npm install
```

4. Environment variables:
- Copy `.env.example` to `.env` in both backend and frontend directories
- Fill in the required environment variables

5. Database setup:
```bash
# Create database and run migrations
cd backend
alembic upgrade head
```

6. Start development servers:

Backend:
```bash
cd backend
uvicorn app.main:app --reload
```

Frontend:
```bash
cd frontend
npm run dev
```

## Configuration

The application requires several environment variables to be set:

### Backend (.env)
```
DATABASE_URL=postgresql://user:password@localhost:5432/ynab_venmo
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_REGION=your_aws_region
YNAB_CLIENT_ID=your_ynab_client_id
YNAB_CLIENT_SECRET=your_ynab_client_secret
EMAIL_DOMAIN=your_email_domain
```

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_YNAB_OAUTH_URL=https://app.ynab.com/oauth/authorize
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 