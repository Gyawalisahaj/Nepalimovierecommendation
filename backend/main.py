"""FastAPI application for movie recommendation system.

This module initializes and configures the FastAPI application with:
- Database connection and initialization
- CORS middleware for frontend communication
- Recommendation routers
"""

import logging
import sys
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import engine, Base
import models
from recommendation import router as recommend_router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize database tables
Base.metadata.create_all(bind=engine)
logger.info("Database initialized successfully")

# Create FastAPI application with metadata
app = FastAPI(
    title="Movie Recommendation Engine",
    description="Advanced ML-powered movie recommendation system using content-based filtering",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# Configure CORS middleware - Allow all origins for Streamlit
origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://localhost:8501",
    "http://127.0.0.1:8501",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Include routers
app.include_router(recommend_router, prefix="/recommend", tags=["Recommendations"])

@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint to verify API is running."""
    return {
        "status": "healthy",
        "service": "Movie Recommendation Engine",
        "version": "1.0.0"
    }

@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint to verify API is running."""
    return {"status": "healthy", "service": "Movie Recommendation API"}
