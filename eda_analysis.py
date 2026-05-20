import pandas as pd

# Load Cleaned Datasets
movies = pd.read_csv('../dataset/cleaned_movies.csv')

ratings = pd.read_csv('../dataset/cleaned_ratings.csv')

# Total Movies
print("Total Movies:")
print(movies.shape[0])

# Total Ratings
print("\nTotal Ratings:")
print(ratings.shape[0])

# Average Rating
print("\nAverage Rating:")
print(ratings['rating'].mean())

# Top Genres
print("\nTop Genres:")
print(movies['genres'].value_counts().head())

# Highest Rated Movies
print("\nTop Rated Movies:")

top_movies = ratings.groupby('movieId')['rating'].mean().sort_values(ascending=False)

print(top_movies.head(10))