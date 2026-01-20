# Movie Recommendation API Documentation

## Overview

MovieFlix is a modern, professionally-built movie recommendation system using content-based filtering with cosine similarity. The backend is built with FastAPI and provides secure authentication via JWT tokens.

## Features

- **JWT Authentication**: Secure token-based authentication with bcrypt password hashing
- **User Registration & Login**: Full user management with email validation
- **Content-Based Recommendations**: Uses TF-IDF vectorization and cosine similarity
- **RESTful API**: Clean, well-documented endpoints
- **CORS Support**: Configured for frontend integration
- **Comprehensive Logging**: Activity tracking for debugging and monitoring
- **Database Persistence**: SQLAlchemy ORM with SQLite

## Technology Stack

- **Framework**: FastAPI
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: JWT (PyJWT) with bcrypt
- **ML/Data**: scikit-learn, pandas, numpy
- **Server**: Uvicorn

## API Endpoints

### Health Check
- **GET** `/health`
  - Check if API is running
  - **Response**: `{"status": "healthy", "service": "Movie Recommendation API"}`

### Authentication

#### Sign Up
- **POST** `/auth/signup`
- **Request**:
  ```json
  {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "password": "securepassword123",
    "confirm_password": "securepassword123"
  }
  ```
- **Response** (201 Created):
  ```json
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "is_active": true
  }
  ```
- **Validation**:
  - Password minimum 8 characters
  - Email must be unique
  - Passwords must match

#### Login
- **POST** `/auth/login`
- **Request**:
  ```json
  {
    "email": "john@example.com",
    "password": "securepassword123"
  }
  ```
- **Response** (200 OK):
  ```json
  {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer",
    "user": {
      "id": 1,
      "first_name": "John",
      "last_name": "Doe",
      "email": "john@example.com",
      "is_active": true
    }
  }
  ```

### Recommendations

#### Get All Movie Titles
- **GET** `/recommend/titles`
- **Response**:
  ```json
  {
    "titles": ["Movie 1", "Movie 2", "Movie 3", ...]
  }
  ```

#### Get Recommendations
- **GET** `/recommend/?movie={title}&limit={count}`
- **Parameters**:
  - `movie` (required): Movie title to get recommendations for
  - `limit` (optional): Number of recommendations (1-20, default: 10)
- **Authentication**: Required (Bearer token)
- **Response** (200 OK):
  ```json
  {
    "current_movie": {
      "title": "Movie Title",
      "genre": "Action, Drama",
      "cast": "Actor 1, Actor 2",
      "director": "Director Name",
      "production_house": "Studio Name",
      "release_date": "2023-01-15",
      "plot": "Movie description...",
      "image_url": "https://...",
      "video_url": "https://..."
    },
    "recommendations": [
      {
        "title": "Recommended Movie 1",
        "genre": "Action",
        "cast": "...",
        "director": "...",
        "production_house": "...",
        "release_date": "...",
        "plot": "...",
        "image_url": "...",
        "video_url": "..."
      }
    ],
    "count": 10
  }
  ```

## Error Responses

### 400 Bad Request
```json
{
  "detail": "Passwords do not match"
}
```

### 401 Unauthorized
```json
{
  "detail": "Could not validate credentials"
}
```

### 404 Not Found
```json
{
  "detail": "Movie 'Invalid Title' not found in database"
}
```

### 409 Conflict
```json
{
  "detail": "Email already registered"
}
```

## Setup & Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Installation Steps

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Server**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

3. **Access API Documentation**
   - Swagger UI: `http://localhost:8000/api/docs`
   - ReDoc: `http://localhost:8000/api/redoc`

## Configuration

### Environment Variables
```bash
export SECRET_KEY="your-secure-secret-key"
export DATABASE_URL="sqlite:///./recommendations.db"
```

### CORS Configuration
The API is configured to accept requests from:
- `http://localhost:5173`
- `http://127.0.0.1:5173`
- `http://localhost:3000`
- `http://127.0.0.1:3000`

Modify `main.py` to add additional allowed origins.

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT true,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## Recommendation Algorithm

The system uses **content-based filtering** with the following approach:

1. **Feature Engineering**: Combines movie attributes (genre, cast, director, production house, plot)
2. **Vectorization**: Uses CountVectorizer with TF-IDF to convert text to numerical vectors
3. **Similarity Calculation**: Computes cosine similarity between movies
4. **Ranking**: Returns top N similar movies

## Security

- Passwords are hashed using bcrypt
- JWT tokens expire after 30 minutes
- Token-based authentication on protected endpoints
- Email validation on registration
- CORS protection against cross-origin attacks

## Logging

The application logs:
- Database initialization
- User registration events
- Login attempts (including failures)
- Recommendation requests
- Error events

Check console output for logs during development.

## Performance

- Movie dataset: Pre-loaded in memory for fast access
- Similarity matrix: Computed once at startup
- Token expiration: 30 minutes per access token
- Response time: < 200ms for recommendations

## Future Enhancements

- User rating system and collaborative filtering
- Advanced recommendation parameters
- Movie ratings and reviews
- Watchlist functionality
- User preferences personalization
- Rate limiting and API quotas

## Support

For issues or questions:
1. Check API documentation at `/api/docs`
2. Review logs for error messages
3. Ensure database file exists and is readable
4. Verify CORS configuration for frontend URL
