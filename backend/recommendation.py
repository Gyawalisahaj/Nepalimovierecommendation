"""Movie recommendation engine using content-based filtering.

This module uses:
- TF-IDF vectorization on movie features
- Cosine similarity to find similar movies
"""

import logging
import pandas as pd
import numpy as np
from fastapi import APIRouter, Query, HTTPException, status
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

logger = logging.getLogger(__name__)

router = APIRouter()

# Load and preprocess movie dataset
try:
    df = pd.read_csv("movies.csv")
    logger.info(f"Loaded {len(df)} movies from dataset")
    
    # Fill missing values
    df["Production House"] = df["Production House"].fillna("N/A")
    df["Director"] = df["Director"].fillna("N/A")
    
    # Create feature matrix
    df1 = df.drop(columns=['Total Ratings', 'Rating'], errors='ignore')
    
    # Combine text features for similarity calculation
    df1['describe'] = (
        df1['Genre'].fillna('') + ' ' +
        df1['Cast'].fillna('') + ' ' +
        df1['Director'].fillna('') + ' ' +
        df1['Production House'].fillna('') + ' ' +
        df1['Plot'].fillna('')
    )
    
    # Clean text data
    def clean_text(x):
        """Normalize text for vectorization."""
        x = x.str.replace(' ', '')
        x = x.str.replace('/', '')
        x = x.str.lower()
        return x
    
    df1['describe'] = clean_text(df1['describe'])
    
    # Clean movie titles
    df['Title'] = df['Title'].str.replace(r'\(\d{4}\)', '', regex=True).str.strip()
    
    # Build similarity matrix
    vectorizer = CountVectorizer(max_features=5000, stop_words='english')
    X = vectorizer.fit_transform(df1['describe']).toarray()
    similarity = cosine_similarity(X)
    logger.info("Similarity matrix computed successfully")
    
except Exception as e:
    logger.error(f"Error loading movie data: {str(e)}")
    df = None
    similarity = None


def get_movie_info(row: pd.Series) -> dict:
    """Extract and format movie information from DataFrame row.
    
    Args:
        row: Movie record from DataFrame
        
    Returns:
        Dictionary with formatted movie details
    """
    return {
        "title": row.get('Title', 'Unknown'),
        "genre": row.get('Genre', 'N/A'),
        "cast": row.get('Cast', 'N/A'),
        "director": row.get('Director', 'N/A'),
        "production_house": row.get('Production House', 'N/A'),
        "release_date": row.get('Release Dates', 'N/A'),
        "plot": row.get('Plot', 'N/A'),
        "image_url": row.get('Image URL') if pd.notna(row.get('Image URL')) else "https://via.placeholder.com/300x450?text=No+Image",
        "video_url": row.get('Movie URL') if pd.notna(row.get('Movie URL')) else None,
    }


@router.get("/titles", summary="Get all available movie titles")
def get_all_titles():
    """Fetch list of all available movie titles.
    
    Returns:
        Dictionary containing list of movie titles
    """
    if df is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Movie database not available"
        )
    titles = df["Title"].dropna().unique().tolist()
    return {"titles": sorted(titles)}


@router.get("/", summary="Get movie recommendations")
def recommend(
    movie: str = Query(..., min_length=1, description="Movie title to get recommendations for"),
    limit: int = Query(10, ge=1, le=20, description="Number of recommendations (1-20)")
):
    """Get movie recommendations based on a selected movie.
    
    Uses content-based filtering with cosine similarity on movie features
    (genre, cast, director, production house, plot).
    
    Args:
        movie: Title of the movie to get recommendations for
        limit: Number of recommendations to return (default: 10)
        
    Returns:
        Dictionary containing current movie and list of recommended movies
        
    Raises:
        HTTPException: If movie not found or database unavailable
    """
    if df is None or similarity is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Movie database not available"
        )
    
    movie_lower = movie.lower().strip()
    
    try:
        # Find movie index
        index = df[df['Title'].str.lower() == movie_lower].index[0]
    except IndexError:
        logger.warning(f"Movie not found: {movie}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Movie '{movie}' not found in database"
        )
    
    # Get similarity scores and find top recommendations
    distances = similarity[index]
    top_indices = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:limit+1]  # Skip the first one (the movie itself)
    
    recommendations = []
    for idx, score in top_indices:
        row = df.iloc[idx]
        recommendations.append(get_movie_info(row))
    
    # Get current movie info
    current_movie = df.iloc[index]
    current_movie_info = get_movie_info(current_movie)
    
    logger.info(f"Generated {len(recommendations)} recommendations for: {movie}")
    
    return {
        "current_movie": current_movie_info,
        "recommendations": recommendations,
        "count": len(recommendations)
    }
