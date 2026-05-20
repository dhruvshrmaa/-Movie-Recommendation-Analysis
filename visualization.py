import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned datasets
movies = pd.read_csv('../dataset/cleaned_movies.csv')

ratings = pd.read_csv('../dataset/cleaned_ratings.csv')

# -------------------------------
# 1. Ratings Distribution Graph
# -------------------------------

plt.figure(figsize=(8,5))

plt.hist(ratings['rating'])

plt.xlabel('Ratings')

plt.ylabel('Count')

plt.title('Movie Ratings Distribution')

plt.show()

# -------------------------------
# 2. Top Rated Movies
# -------------------------------

top_movies = ratings.groupby('movieId')['rating'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))

top_movies.plot(kind='bar')

plt.xlabel('Movie ID')

plt.ylabel('Average Rating')

plt.title('Top Rated Movies')

plt.show()

# -------------------------------
# 3. Top Genres
# -------------------------------

top_genres = movies['genres'].value_counts().head(10)

plt.figure(figsize=(10,5))

top_genres.plot(kind='bar')

plt.xlabel('Genres')

plt.ylabel('Count')

plt.title('Top Genres')

plt.show()