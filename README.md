# 🔍 AI Semantic Search using Endee

## 📌 Project Overview

This project implements a **Semantic Search System** using a vector database approach inspired by Endee. It allows users to search relevant information from a dataset using natural language queries instead of exact keyword matching.

The system converts text into embeddings and retrieves the most similar results based on user input.

---

## 🚀 Features

* 🔎 Semantic search using embeddings
* ⚡ Fast similarity-based retrieval
* 🧠 Uses transformer-based NLP model
* 💻 Simple and interactive UI using Streamlit
* 📂 Works with structured text datasets

---

## 🧠 Technologies Used

* Python
* Streamlit
* Sentence Transformers
* NumPy
* Endee (Vector Database concept)

---

## 🏗️ System Architecture

1. Load dataset (text data)
2. Convert text into vector embeddings
3. Store embeddings in vector database
4. Accept user query
5. Convert query into embedding
6. Perform similarity search
7. Display top matching results

---

## 📂 Project Structure

```
endee-project/
│
├── app.py
├── requirements.txt
├── README.md
│
└── data/
    └── sample.txt
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone https://github.com/abinanthana005/endee.git
cd endee
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```
streamlit run app.py
```

---

## 💡 How It Works

* The dataset is loaded from a text file
* Each sentence is converted into embeddings using a pre-trained model
* User query is also converted into embedding
* Cosine similarity is used to find the closest matches
* Top results are displayed in the UI

---

## 📊 Use Case

This project can be used for:

* 📚 Notes search system
* 📄 Document retrieval
* 🤖 AI-powered search engines
* 📖 Knowledge base search

---

## 🔗 Endee Integration

This project follows the concept of using Endee as a vector database for storing and retrieving embeddings efficiently. It demonstrates how semantic search can be implemented using vector similarity.

---

## 📌 Future Improvements

* ✅ Integrate real Endee vector database
* ✅ Add chatbot (RAG-based system)
* ✅ Upload custom datasets
* ✅ Improve UI/UX

---

## 👩‍💻 Author

**Abinanthana**

---

## ⭐ Acknowledgment

Special thanks to the Endee project for providing a foundation for vector-based search systems.
