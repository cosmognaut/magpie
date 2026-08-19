# I WANT TO EDIT THE NAMES OF THE GENRES
import pandas as pd

original = pd.read_parquet('data/clustered_watch_later.parquet')
df = original.copy()
"""
CLUSTERS TO BE MERGED // GENRES:
    (more fun with more specific genres)
-1 - Mixed bag
0 - Philosophy
*1 - very miscellaneous maybe Internet, maybe -1
2 - Pokemon
3 and 4 - Food
5 - Exercise
6 and 7 - Physics
8, 10, 11 - Mathematics (9 was entirely math sorcerer, just tagging it for now)
12 and 13 and 14 - Creativity (movies, etc.)
17 - Technology
18 - Mindset and Thinking - think of a better name.
15 and 16 and 20 and 21 and 22 - Learning and Productivity
*23 - very miscellaneous - some music, some internet some learning. Maybe -1
24 and 26 - Programming
25 and 38 and 19 - Video Essays
27 and 28 - Linux and Tooling
29 and 30 - General gaming
31 - Horror Games
32 - Earth and Anomlaies 
33 - Japanese Culture
34 - Money and World Models
35 - Countries and Progress
36 and 37 - The Sounds of Life 
*39 - Maybe -1 i.e. mixed bag 
40 and 41 - The Internet
42 - Dark History 
"""
def assign_genre(series: pd.Series):
    cluster = series['genre_cluster']
    if cluster == 0:
        genre = "Philosophy"
    elif cluster == 2:
        genre = "Pokémon"
    elif cluster in (3, 4):
        genre = "Food"
    elif cluster == 5:
        genre = "Exercise"
    elif cluster in (6, 7):
        genre = "Physics"
    elif cluster in (8, 9, 10, 11):
        genre = "Mathematics"
    elif cluster in (12, 13, 14):
        genre = "Creativity"
    elif cluster in (15, 16, 20, 21, 22):
        genre = "Learning and Productivity"
    elif cluster == 17:
        genre = "Technology"
    elif cluster == 18:
        genre = "Mindset and Thinking"
    elif cluster in (19, 25, 38):
        genre = "Video Essays"
    elif cluster in (24, 26):
        genre = "Programming"
    elif cluster in (27, 28):
        genre = "Linux and Tooling"
    elif cluster in (29, 30):
        genre = "General Gaming"
    elif cluster == 31:
        genre = "Horror Games"
    elif cluster == 32:
        genre = "Earth and Anomlaies"
    elif cluster == 33:
        genre = "Japanese Culture"
    elif cluster == 34:
        genre = "Money and World Models"
    elif cluster == 35:
        genre = "Countries and Progress"
    elif cluster in (36, 37):
        genre = "The Sounds of Life"
    elif cluster in (40, 41):
        genre = "The Internet"
    elif cluster == 42:
        genre = "Dark History"
    else:
        genre = "Mixed Bag" 
    # if cluster in (-1, 1, 23, 39):
    #     genre = "Mixed Bag"
    return genre

df['genre'] = df.apply(assign_genre, axis=1)

print(df.tail())

df.to_parquet('assigned_genres.parquet')
