import pandas as pd

movies = pd.read_csv(
    '../dataset/movies.csv',
    sep='::',
    engine='python',
    encoding='latin1',
    header=None
)

ratings = pd.read_csv(
    '../dataset/ratings.csv',
    sep='::',
    engine='python',
    encoding='latin1',
    header=None
)

print("Movies Dataset")
print(movies.head())

print("Ratings Dataset")
print(ratings.head())