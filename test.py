import pandas as pan

df: pan.DataFrame = pan.read_csv('backend/video.csv')
print(df.head())
print(df['tags'])
