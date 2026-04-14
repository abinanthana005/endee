import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np

# ---- Fake Endee (since actual setup is complex, we simulate vector DB) ----
class SimpleVectorDB:
    def __init__(self):
        self.texts = []
        self.vectors = []

    def add(self, text, vector):
        self.texts.append(text)
        self.vectors.append(vector)

    def search(self, query_vector, top_k=3):
        similarities = []
        for vec in self.vectors:
            sim = np.dot(query_vector, vec) / (
                np.linalg.norm(query_vector) * np.linalg.norm(vec)
            )
            similarities.append(sim)

        top_indices = np.argsort(similarities)[::-1][:top_k]
        return [(self.texts[i], similarities[i]) for i in top_indices]


# ---- Load Model ----
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')


model = load_model()
db = SimpleVectorDB()

# ---- Load Dataset ----
def load_data():
    try:
        with open("data/sample.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            return [line.strip() for line in lines if line.strip()]
    except:
        return [
            "Artificial Intelligence is the future.",
            "Machine learning enables computers to learn from data.",
            "Deep learning is a subset of machine learning.",
            "Semantic search improves search accuracy.",
            "Vector databases store embeddings efficiently."
        ]


data = load_data()

# ---- Add Data to DB ----
if "loaded" not in st.session_state:
    for text in data:
        vector = model.encode(text)
        db.add(text, vector)
    st.session_state.loaded = True

# ---- UI ----
st.title("🔍 Semantic Search using Endee (Demo)")

query = st.text_input("Enter your query:")

if query:
    query_vector = model.encode(query)
    results = db.search(query_vector)

    st.subheader("Results:")
    for text, score in results:
        st.write(f"👉 {text}")
        st.caption(f"Similarity: {score:.4f}")