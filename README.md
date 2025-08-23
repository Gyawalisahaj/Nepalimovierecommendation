# Nepali Movie Recommendation System

A **content-based movie recommendation system** for Nepali movies built using **FastAPI**, **React/TypeScript**, and **scikit-learn**.  
The system recommends movies based on **genre, cast, director, production house, and plot**.

---

## 🗂 Project Structure

asd/
├── backend/
│   ├── __init__.py
│   ├── auth.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── movies.csv
│   ├── recommendation.py
│   ├── requirements.txt
│   ├── test.db
│   └── __pycache__/
│       ├── __init__.cpython-313.pyc
│       ├── auth.cpython-313.pyc
│       ├── database.cpython-313.pyc
│       ├── main.cpython-313.pyc
│       ├── models.cpython-313.pyc
│       └── ...
├── frontend/
│   ├── .gitignore
│   ├── eslint.config.js
│   ├── index.html
│   ├── package.json
│   ├── README.md
│   ├── tsconfig.app.json
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   ├── vite.config.ts
│   ├── public/
│   │   └── vite.svg
│   └── src/
│       └── ...
├── ml/
│   ├── movierecommendation.ipynb
│   └── .ipynb_checkpoints/


Features:

Search Movies – Users can search for Nepali movies by typing the title in the search bar.
![EDA](ml/recommendation4.png)

Autocomplete Suggestions – Shows matching movie titles as you type for faster selection.

Top 5 Recommendations – Provides top 5 similar movies based on genre, cast, director, production house, and plot.

Detailed Movie Info – Each recommended movie displays:

Title

Genre

Cast

Director

Production House

Release Date

Plot Summary

Image and Video URL (if available)

User Authentication – Secure access using JWT-based login and registration.

Default Handling – Automatically handles missing values like images or production house info.

Responsive Frontend – Mobile-friendly React/TypeScript interface with TailwindCSS.

Data-Driven Recommendations – Uses content-based filtering with cosine similarity for relevant suggestions.
