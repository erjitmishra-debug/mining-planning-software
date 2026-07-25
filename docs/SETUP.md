# Setup Guide

## Prerequisites

- Python 3.9+ or Node.js 16+
- PostgreSQL 12+ or MongoDB 4.4+
- Git
- Docker (optional but recommended)

## Installation

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

### Using Docker

```bash
docker-compose up
```

## Configuration

1. Copy `.env.example` to `.env`
2. Update database connection strings
3. Configure API endpoints
4. Set up authentication (JWT/OAuth)

## Database Schema

The application uses the following main entities:
- **Mines**: Mining sites and operations
- **Resources**: Coal seams, ore bodies, mineral deposits
- **Equipment**: Excavators, loaders, trucks, drills
- **Workforce**: Employees, contractors, shifts
- **Production**: Daily/monthly production records
- **Financial**: Costs, revenues, budgets
- **Safety**: Incidents, metrics, compliance

## Running Tests

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

## Deployment

See [DEPLOYMENT.md](./DEPLOYMENT.md) for production deployment guidelines.
