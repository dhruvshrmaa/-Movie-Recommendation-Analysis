import pandas as pd

# Load cleaned data
movies = pd.read_csv('../dataset/cleaned_movies.csv')
ratings = pd.read_csv('../dataset/cleaned_ratings.csv')

# Average rating per movie
movie_stats = ratings.groupby('movieId')['rating'].agg(['mean', 'count'])

movie_stats = movie_stats.sort_values(by='mean', ascending=False)

print("Top Recommended Movies:")
print(movie_stats.head(10))