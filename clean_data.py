import pandas as pd

# Load Movies Dataset
movies = pd.read_csv(
    '../dataset/movies.csv',
    sep='::',
    engine='python',
    encoding='latin1',
    header=None
)

# Load Ratings Dataset
ratings = pd.read_csv(
    '../dataset/ratings.csv',
    sep='::',
    engine='python',
    encoding='latin1',
    header=None
)

# Column Names
movies.columns = ['movieId', 'title', 'genres']
ratings.columns = ['userId', 'movieId', 'rating', 'timestamp']

# Remove duplicates
movies.drop_duplicates(inplace=True)
ratings.drop_duplicates(inplace=True)

# Remove null values
movies.dropna(inplace=True)
ratings.dropna(inplace=True)

# Save cleaned datasets
movies.to_csv('../dataset/cleaned_movies.csv', index=False)

ratings.to_csv('../dataset/cleaned_ratings.csv', index=False)

print("Data Cleaning Completed Successfully")