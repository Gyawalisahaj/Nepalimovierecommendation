import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import json

# Page configuration
st.set_page_config(
    page_title="MovieFlix - AI Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .stTitle {
        color: #FF6B35;
        font-size: 3rem;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .movie-card {
        padding: 1.5rem;
        border-radius: 10px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin: 0.5rem 0;
    }
    .metric-card {
        padding: 1rem;
        border-radius: 8px;
        background: #f0f2f6;
        text-align: center;
    }
    .stat-number {
        font-size: 1.8rem;
        font-weight: bold;
        color: #FF6B35;
    }
    </style>
""", unsafe_allow_html=True)

# API Configuration
API_BASE_URL = "https://nepalimovierecommendation.vercel.app/"

# Session state
if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None
if "recommendations" not in st.session_state:
    st.session_state.recommendations = []
if "current_movie" not in st.session_state:
    st.session_state.current_movie = None

# Header
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("# 🎬 MovieFlix")
    st.markdown("### AI-Powered Movie Recommendation Engine")
    st.markdown("*Discover movies you'll love using advanced ML algorithms*")

st.divider()

st.header("ℹ️ Statistics")
try:
    response = requests.get(f"{API_BASE_URL}/health", timeout=5)
    if response.status_code == 200:
        st.success("✅ Backend API Connected")
    else:
        st.error("❌ Backend Error")
except:
    st.error("❌ Backend Not Available")

# Main content
st.header("🔍 Find Your Next Favorite Movie")

# Try to fetch all titles
try:
    response = requests.get(f"{API_BASE_URL}/recommend/titles", timeout=10)
    response.raise_for_status()
    all_titles = response.json().get("titles", [])
    
    if all_titles:
        # Movie selection
        col1, col2 = st.columns([3, 1])
        
        with col1:
            selected_movie = st.selectbox(
                "",
                options=sorted(all_titles),
                key="movie_selector"
            )
        
        with col2:
            search_button = st.button(
                ""
                "🔎 Search"
                "",
                use_container_width=True,
                type="primary",
                key="search_btn"
            )
        
        st.divider()

        
        # Get recommendations
        if search_button or selected_movie != st.session_state.selected_movie:
            st.session_state.selected_movie = selected_movie
            
            with st.spinner(f"🎬 Finding recommendations for '{selected_movie}'..."):
                try:
                    response = requests.get(
                        f"{API_BASE_URL}/recommend/",
                        params={"movie": selected_movie, "limit": 10},
                        timeout=15
                    )
                    response.raise_for_status()
                    data = response.json()
                    
                    st.session_state.current_movie = data.get("current_movie")
                    st.session_state.recommendations = data.get("recommendations", [])
                    
                except requests.exceptions.RequestException as e:
                    st.error(f"❌ Error fetching recommendations: {str(e)}")
                    st.session_state.recommendations = []
        
        # Display current movie
        if st.session_state.current_movie:
            st.subheader("🎯 Selected Movie")
            
            movie = st.session_state.current_movie
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                if movie.get("image_url"):
                    st.image(
                        movie["image_url"],
                        width=250,
                        caption=movie.get("title", "Movie")
                    )
            
            with col2:
                st.markdown(f"### {movie.get('title', 'N/A')}")
                
                col_a, col_b = st.columns(2)
                with col_a:
                    st.metric("Genre", movie.get("genre", "N/A"))
                    st.metric("Director", movie.get("director", "N/A"))
                with col_b:
                    st.metric("Release Date", movie.get("release_date", "N/A"))
                    st.metric("Production", movie.get("production_house", "N/A"))
                
                with st.expander("📖 Plot Summary"):
                    st.write(movie.get("plot", "N/A"))
                
                with st.expander("🎭 Cast"):
                    st.write(movie.get("cast", "N/A"))
                
                if movie.get("video_url"):
                    st.markdown(f"[▶️ Watch Movie]({movie['video_url']}) 🎥")
        st.divider()


        
        # Display recommendations
        if st.session_state.recommendations:
            st.divider()
            st.subheader(f"✨ Top {len(st.session_state.recommendations)} Recommendations")
            
            # Display as cards in columns
            cols = st.columns(2)
            for idx, movie in enumerate(st.session_state.recommendations):
                with cols[idx % 2]:
                    with st.container(border=True):
                        st.markdown(f"### {movie.get('title', 'N/A')}")
                        
                        if movie.get("image_url"):
                            st.image(
                                movie["image_url"],
                                width=200,
                                caption="Movie Poster"
                            )
                        
                        col_info1, col_info2 = st.columns(2)
                        with col_info1:
                            st.caption(f"**Genre:** {movie.get('genre', 'N/A')}")
                            st.caption(f"**Director:** {movie.get('director', 'N/A')}")
                        with col_info2:
                            st.caption(f"**Release:** {movie.get('release_date', 'N/A')}")
                            st.caption(f"**Production:** {movie.get('production_house', 'N/A')}")
                        
                        with st.expander("📖 Plot"):
                            st.caption(movie.get("plot", "N/A"))
                        
                        with st.expander("🎭 Cast"):
                            st.caption(movie.get("cast", "N/A"))
                        
                        if movie.get("video_url"):
                            st.markdown(
                                f"[▶️ Watch]({movie['video_url']}) | "
                                f"[More Info](https://www.imdb.com/search/title/)",
                                unsafe_allow_html=False
                            )
    else:
        st.warning("⚠️ No movies available in the database")
        
except requests.exceptions.ConnectionError:
    st.error("❌ Cannot connect to backend API. Make sure the backend server is running on http://127.0.0.1:8000")
except Exception as e:
    st.error(f"❌ Error: {str(e)}")

# Footer - About the Project
st.divider()

with st.container():
    st.header("📽️ About the Project")
    st.markdown("""
    **MovieFlix** is a professional, full-stack **content-based movie recommendation system**
    developed using a **FastAPI backend** and a **Streamlit frontend**.  
    The system intelligently recommends movies by analyzing **genre, cast, director,
    production house, and plot**.
    """)

    st.markdown("### ✨ Highlights")
    st.markdown("""
    - Uses content-based filtering for personalized recommendations  
    - Implements TF-IDF vectorization and cosine similarity  
    - Interactive and responsive Streamlit web interface  
    - FastAPI-powered backend for real-time results  
    - No authentication required for instant access  
    - Smart movie search with full dataset coverage  
    - Jupyter Notebook documentation explaining the ML workflow  
    """)

    st.markdown("### 🔍 Recommendation Logic")
    st.markdown("""
    - Extracts important movie features  
    - Converts textual data into numerical vectors  
    - Computes similarity scores between movies  
    - Ranks and returns the most relevant recommendations  
    """)

    st.divider()

    st.markdown(
    "<center><b>MovieFlix</b> © 2026 | A Machine Learning Project by Sahaj Gyawali | "
    "<a href='https://github.com/Gyawalisahaj/Nepalimovierecommendation' target='_blank'>GitHub</a></center>",
    unsafe_allow_html=True
   )


