# YNAB-Venmo Integration

Automatically import Venmo transactions into YNAB (You Need A Budget) by forwarding email notifications.


## Tech Stack

### Backend
- FastAPI (Python)
- Supabase for PostgresSQL database
- Sendgrid for maintaining email addresses
- YNAB API integration

### Frontend
- Next.js
- TypeScript
- Tailwind CSS


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
pnpm install 
```

4. Environment variables:
- change `.env.example` to `.env.local` in both directories. 
- fill in the needed env variables. 

5. Database setup:
```bash
# Create database and run migrations
cd backend
alembic upgrade head
```

6. Start development servers:
If on a mac and using iTerm2, run `./setup.sh` to create a 4-paned window running the frontend and backend servers, with additional panes for git management and backend shell commands. It also opens windows in Google Chrome to show the local development servers.

```
+-----------+----------+
| /frontend | .        |
| nextjs    | (git)    |
| server    |          |
+-----------+----------+
| /backend  | /backend |
| fastapi   | shell    |
| server    |          |
+-----------+----------+
```

**Manual setup**

Backend:
```bash
cd backend
fastapi dev main.py
```

Frontend:
```bash
cd frontend
pnpm dev
```