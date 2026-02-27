# 🎬 MovieFlix - AI Movie Recommendation System

A professional, full-stack **content-based movie recommendation system** built with **FastAPI** backend and **Streamlit** frontend. The system recommends movies based on **genre, cast, director, production house, and plot** using intelligent similarity algorithms.


---

## ✨ Key Features

🎯 **Intelligent Recommendations** – Content-based filtering using TF-IDF vectorization and cosine similarity  
🎬 **Streamlit UI** – Modern, interactive web interface with instant results  
⚡ **No Authentication** – Simplified architecture for instant access  
🔍 **Smart Search** – Movie dropdown with complete database access  
📊 **Live API Integration** – Real-time backend communication  
💡 **Well-Documented** – Jupyter notebooks for ML algorithm explanation  

## 🗂️ Project Structure

```
recommendation/
├── app.py                      # Streamlit Frontend (Port 8501)
│
├── backend/                    # FastAPI Backend (Port 8000)
│   ├── main.py                # Application setup & CORS
│   ├── recommendation.py      # ML engine & endpoints
│   ├── models.py              # SQLAlchemy ORM models
│   ├── movies.csv             # Movie dataset (500+ titles)
│   ├── requirements.txt       # Python dependencies
│   └── venv/                  # Virtual environment
│
├── ml/                         # ML Model Documentation
│   ├── movierecommendation.ipynb  # Jupyter notebook with algorithm analysis
│   └── *.png                  # Visual documentation & diagrams
│
├── screenshot/                # Project screenshots
│
└── README.md                  # This file
```

---

## 🚀 Quick Start (2 Minutes)

### Prerequisites
- **Python 3.8+** with pip
- **Git** for version control

### Step 1: Clone & Setup

```bash
cd /path/to/recommendation
python -m venv venv
source venv/bin/activate  # Linux/Mac
# OR: venv\Scripts\activate  (Windows)
```

### Step 2: Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
cd ..
```

### Step 3: Start Backend (Port 8000)

```bash
cd backend
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

**Output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

### Step 4: Start Streamlit Frontend (Port 8501)

Open another terminal:

```bash
pip install streamlit requests --quiet
streamlit run app.py --server.port=8501
```

**Output:**
```
Local URL: http://localhost:8501
```

### Step 5: Open Application

Navigate to: **http://localhost:8501**

---

## 📖 Usage Guide

### Using the Streamlit Interface

1. **Select a Movie**
   - Open dropdown menu
   - Choose any movie from 500+ database
   - Instant preview loads

2. **View Recommendations**
   - System generates 10 similar movies
   - Shows match percentage for each
   - Displays movie posters and details

3. **Explore Movie Info**
   - Click "Show Plot" to expand details
   - View genre, director, cast, release date
   - Click "Watch on..." to access movie

### Screenshots

**Main Interface:**
![MovieFlix Home](./screenshot/recommendation1.png)

**Recommendations Display:**
![Recommendations](./screenshot/recommendation2.png)

**ML Model (For Interviews):**
![ML Algorithm](./screenshot/recommended_model.png)

---

## 🤖 ML Recommendation Algorithm

The system uses **Content-Based Filtering** for intelligent recommendations.

### How It Works

```
Step 1: Feature Engineering
   ├─ Extract: Genre + Cast + Director + Production House + Plot
   ├─ Clean: Remove special chars, normalize text
   └─ Combine: Concatenate all features

Step 2: Vectorization (TF-IDF)
   ├─ Convert text to numerical vectors
   ├─ Create 5000-dimensional feature space
   └─ Use scikit-learn CountVectorizer

Step 3: Similarity Matrix
   ├─ Compute cosine similarity between all movies
   ├─ Create n×n similarity matrix (n = 500+)
   └─ Pre-compute on app startup for speed

Step 4: Recommendations
   ├─ User selects movie
   ├─ Fetch similarity scores for that movie
   ├─ Sort by similarity (descending)
   └─ Return top 10 recommendations with scores
```

### Algorithm Details

**Vectorization:** TF-IDF (Term Frequency-Inverse Document Frequency)
- Weights important words higher
- Removes common English stopwords
- 5000 maximum features

**Similarity:** Cosine Similarity
- Range: 0 to 1 (0 = no similarity, 1 = identical)
- Measures angle between feature vectors
- Computationally efficient

**Example:**
```
Selected: "Inception" (Sci-Fi, Leonardo DiCaprio, Nolan)
    ↓
Find movies with similar: Genre, Cast, Director, Plot
    ↓
Similarity Scores:
   - The Dark Knight (0.89) ✓ Highest match
   - Interstellar (0.87)
   - The Matrix (0.76)
   - ... and 7 more
```

---

## 📊 Dataset

- **500+ movies** in database
- Fields: Title, Genre, Cast, Director, Release Date, Plot, IMDb Rating, Image URL
- Data source: Movie CSV file
- Pre-processed and cleaned for ML


---

## 🛠️ Technology Stack

### Backend
| Technology | Purpose | Version |
|-----------|---------|---------|
| **FastAPI** | Web framework | Latest |
| **Pandas** | Data processing | 1.x |
| **scikit-learn** | ML algorithms | 1.x |
| **Uvicorn** | ASGI server | Latest |

### Frontend
| Technology | Purpose | Version |
|-----------|---------|---------|
| **Streamlit** | UI framework | 1.28+ |
| **Requests** | HTTP client | 2.x |
| **Python** | Runtime | 3.8+ |


---

## 🎨 Streamlit UI Features

- **Movie Dropdown** – Select from 500+ titles instantly
- **Real-time Recommendations** – Get 10 similar movies in seconds
- **Movie Metadata** – Genre, director, cast, release date displayed
- **Match Percentage** – See similarity score for each recommendation
- **Movie Posters** – Visual representation with 2-column grid layout
- **Responsive Design** – Works on desktop and mobile
- **Expandable Details** – Click to expand plot and full information

---

## 🚦 Startup Guide
## create venv
```bash
python -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
```

### Terminal 1 - Start Backend

```bash
cd /path/to/recommendation/backend
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Expected output:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
INFO:main:Database initialized successfully
```

### Terminal 2 - Start Frontend

```bash
cd /path/to/recommendation
streamlit run app.py --server.port=8501
```

Expected output:
```
Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

### Step 3 - Open Browser

Navigate to: **http://localhost:8501**

---


