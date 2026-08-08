import joblib
import hdbscan
from sentence_transformers import SentenceTransformer

MODEL = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
pipeline = joblib.load('genre_pipeline.pkl')

sentence = [
    "Something related to programming and Linux, also C++ and Python and Rust"
]

embedding = MODEL.encode(sentence)
UMAP = pipeline[0]

reduced = UMAP.transform(embedding)
labels, probabilities = hdbscan.approximate_predict(clusterer=pipeline[1], points_to_predict=reduced)

print(labels)

print(f"Cluster: {labels[0]}")
